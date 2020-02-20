document.addEventListener('DOMContentLoaded', () => {    
    const solicitud = document.getElementById('solicitudes');
    const diasdisp = document.getElementById('dias');
    const horavisi = document.getElementById('horario');
    const comite = document.getElementById('idcomite');
    const voluntario = document.getElementById('idvoluntario');

    $('#solicitudes').change(async function() {
        const idsolicitud = solicitud.value;
        if (idsolicitud != '') {
            const {horavisi, lunes, martes, miercoles, jueves, viernes, sabado, domingo} = await solicitudId(idsolicitud);
            let dias =  `${lunes ? 'Lunes,':''}${martes ? 'Martes,':''}${miercoles ? 'Miercoles,':''}
            ${jueves ? 'Jueves,':''}${viernes ? 'Viernes,':''}${sabado ? 'Sabado,':''}
            ${domingo ? 'Domingo,':''} `;
            $('#dias').val(`${dias.replace(/\s/g,'')}`);
            $('#horario').val(horavisi);
        }
    });
  
    const solicitudId = async(id) => {
        try {
            const res = await fetch(`/actividades/solicitud_hospital/get_solicitudes_json_id/${id}`);
            const data = await res.json();            
            return data;
        } catch (error) {
            console.log(error);
        }
    }
});

// Codigo para Vue
// Esto ayuda a controlar que vue entienda a Select2
Vue.directive('select', {
    twoWay: true,
    bind: function (el, binding, vnode) {
      $(el).select2().on("select2:select", (e) => {
        // v-model looks for
        //  - an event named "change"
        //  - a value with property path "$event.target.value"
        el.dispatchEvent(new Event('change', { target: e.target }));
      });
    },
});

var app = new Vue({
    el: '#app'
    , data: {
        lista: []
        , lista_voluntarios: []
        , lista_editar:[]
        , idcomite: ''
        , comite:''
        , idvoluntario: ''
        , voluntario: ''
        , solicitudes: ''
        , fechavisita: ''
        , horavisita: ''
        , obs: ''
        , editar: false
    }
    , methods: {
        obtenerVoluntarios: async function () {            
            try {
                if (this.idcomite != '') {
                    const res = await fetch(`/actividades/solicitud_hospital/get_integrantes_comite/${this.idcomite}`);
                    const data = await res.json();            
                    const datos = data;           
                    if (datos != null || datos != undefined) {
                        $('#agregar').prop('disabled', false);
                        for(let voluntario of datos) {
                            const { idcomite, comite, idpersona, nombres, apellidos } = voluntario;
                            this.lista_voluntarios.push({
                                text: `${nombres} ${apellidos}`, value: idpersona                                
                            });
                        }
                    } else {
                        this.lista_voluntarios = [];
                        $('#agregar').prop('disabled', true);
                    }
                } else {
                    this.lista_voluntarios = [];
                    $('#agregar').prop('disabled', true);
                }
            } catch (error) {
                console.log(error);
            }            
        }
        , agregarVoluntario: function () {            
            let encontrado = false;
            if (this.voluntario != '') {
                $('#idcomite').prop('disabled', true);
                if (this.lista.length > 0) {
                    for(let item of this.lista) {                        
                        if(item.value == this.voluntario.id && item.text == this.voluntario.texto) {                            
                            encontrado = true;
                        } 
                    }
                    if (!encontrado) {
                        this.lista.push({
                            value: this.voluntario.id
                            , text: this.voluntario.texto
                        });                        
                        $('#voluntario').val(null).trigger('change');
                    } else {
                        alert('Ya existe');
                        $('#voluntario').val(null).trigger('change');
                    }
                } else {                    
                    this.lista.push({
                        value: this.voluntario.id
                        , text: this.voluntario.texto
                    });
                }               
            this.voluntario = '';
            } else {                
                alert('Favor elige un voluntario');
            }
        }
        , agregarVoluntarioE: async function () {
            //Enviar datos a la BD
            const conf = confirm('Desea agregar ?');
            if (conf) {  
                const datos = {
                    idlista: localStorage.getItem('idlista')
                    , idvoluntario: this.voluntario.id
                }                                            
                try {
                    const res = await axios(`/actividades/solicitud_hospital/agregar_voluntario/${datos.idlista}/${datos.idvoluntario}`);
                    console.log(res);
                    if(res.data.estado==true){
                        location.href = `/actividades/solicitud_hospital/modificar_voluntarios/${idlista}`;
                    }
                } catch (error) {
                    console.log(error);
                }
            }
        }
        , eliminarBDVoluntario: async function (idlista, idvoluntario) {
            //Enviar datos a la BD
            const conf = confirm('Desea eliminar ?');
            if (conf) {                               
                try {
                    const res = await axios(`/actividades/solicitud_hospital/eliminar_voluntario/${idlista}/${idvoluntario}`);
                    console.log(res);
                    if(res.data.estado==true){
                        location.href = `/actividades/solicitud_hospital/modificar_voluntarios/${idlista}`;
                    }
                } catch (error) {
                    console.log(error);
                }
            }
        }
        , eliminarVoluntario: function (id, texto) {            
            const conf = confirm(`Desea eliminar a ${texto}`);
            if (conf) {
                const removeIndex = this.lista.map(function (item) {                
                    return item.value;
                }).indexOf(id);
                this.lista.splice(removeIndex, 1);
            }
            if (this.lista.length == 0) {
                $('#idcomite').prop('disabled', false);
            }
        }
        , enviarDatos: async function () {
            if (this.solicitudes == '') {
                alert('Debe escoger una solicitud');
                $('#solicitudes').focus();
                return;
            }
            if (this.fechavisita == '') {
                alert('Debe escoger una fecha');
                $('#fechavisita').focus();
                return;
            }
            if (this.horavisita == '') {
                alert('Debe escoger una hora');
                $('#horavisita').focus();
                return;
            }
            if (this.lista.length == 0) {
                alert('Debe agregar voluntarios a esta solicitud');
                $('#idcomite').focus();
                return;
            }
            alert('Formulario correcto, enviando datos');
            const datos = {
                idsolicitud: this.solicitudes
                , idcomite: this.idcomite
                , fechavisita: this.fechavisita
                , horavisita: this.horavisita
                , obs: this.obs
                , voluntarios: this.lista
            }            
            try {
                const res  = await fetch('/actividades/solicitud_hospital/registar_lista', {
                    method:'POST'
                    , headers:{
                        'Content-Type':'application/json'
                    }
                    , body:JSON.stringify(datos)
                });
                const data = await res.json();
                console.log(data);
                if (data.estado == true) {
                    location.href = '/actividades/solicitud_hospital/voluntarios';
                }
            } catch (error) {
                console.error(error);
            }
        }
        , actualizarDatos: async function () {
            if (this.solicitudes == '') {
                alert('Debe escoger una solicitud');
                $('#solicitudes').focus();
                return;
            }
            if (this.fechavisita == '') {
                alert('Debe escoger una fecha');
                $('#fechavisita').focus();
                return;
            }
            if (this.horavisita == '') {
                alert('Debe escoger una hora');
                $('#horavisita').focus();
                return;
            }
            alert('Formulario correcto, enviando datos');
            const datos = {
                idsolicitud: this.solicitudes
                , fechavisita: this.fechavisita
                , horavisita: this.horavisita
                , obs: this.obs
            }  
            try {
                const res = await axios.put('/actividades/solicitud_hospital/actualizar_lista_voluntario', datos);
                if(res.data.estado==true) {
                    location.href = '/actividades/solicitud_hospital/voluntarios';
                }
            } catch (error) {
                console.error(error);
            }
        }
        , cargarFormulario: async function () {
            const idlista = localStorage.getItem('idlista');
            try {
                const res = await axios.get(`/actividades/solicitud_hospital/obtener_lista_voluntarios/${idlista}`);
                const {idsolicitud, horavisita, fechavisita, obs, idcomite} = await res.data;                
                this.lista_editar = await res.data;
                this.fechavisita = fechavisita;
                this.horavisita = horavisita;
                this.obs = obs;
                this.solicitudes = idsolicitud;
                this.idcomite = idcomite;
                this.obtenerVoluntarios();
                this.editar = true;
                $('#solicitudes').val(idsolicitud);
                $('#solicitudes').trigger('change');
                $('#idcomite').val(idcomite);
                $('#idcomite').trigger('change');
            } catch (error) {
                console.error(error);
            }
        }
    }
    , beforeMount() {
        this.cargarFormulario();
    }
    , computed: {   
    }, delimiters: ['[[',']]']
});

$('select').select2({});