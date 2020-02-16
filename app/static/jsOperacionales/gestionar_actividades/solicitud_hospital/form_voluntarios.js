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
        , idcomite: ''
        , comite:''
        , idvoluntario: ''
        , voluntario: ''
        , solicitudes: ''
        , fechavisita: ''
        , horavisita: ''
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
        , enviarDatos: function () {
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
                , fechavisita: this.fechavisita
                , horavisita: this.horavisita
                , voluntarios: this.lista
            }
            console.log(datos);
        }
    }
    , beforeMount() {
        //this.obtenerVoluntarios();
    }
    , computed: {   
    }, delimiters: ['[[',']]']
});

$('select').select2({});