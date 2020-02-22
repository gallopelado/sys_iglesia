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
        , solicitudes:[]
        , dataEnvio: {}
        , voluntario: ''
        , descripcion: ''
        , editar: false
    }
    , methods: {
        obtenerVoluntarios: async function () { 
            this.lista_voluntarios = [];           
            try {
                if (this.idcomite != '') {
                    const res = await fetch(`/actividades/solicitud_hospital/get_integrantes_comite/${this.solicitudes}`);
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
        , enviarDatos: async function () {
            if (this.solicitudes == '') {
                alert('Debe escoger una solicitud');
                $('#solicitudes').focus();
                return;
            }
            if (this.voluntario == '') {
                alert('Debe escoger una voluntario');
                $('#voluntario').focus();
                return;
            }
            if (this.descripcion == '') {
                alert('Falta escribir descripcion');
                $('#descripcion').focus();
                return;
            }
            this.dataEnvio = {
                idsolicitud: this.solicitudes
                , voluntarios: this.voluntario.id
                , descripcion: this.descripcion.toUpperCase()
            }            
            try {
                const res  = await axios.post('/actividades/solicitud_hospital/nuevo_informe', this.dataEnvio);                
                console.log(res);
                if(res.data.estado==true) {
                    location.href = '/actividades/solicitud_hospital/informevisitas';
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
        //this.cargarFormulario();
    }
    , computed: {   
    }, delimiters: ['[[',']]']
});

$('select').select2({});