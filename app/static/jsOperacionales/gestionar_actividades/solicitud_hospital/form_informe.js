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
                        for(let voluntario of datos) {
                            const { idcomite, comite, idpersona, nombres, apellidos } = voluntario;
                            this.lista_voluntarios.push({
                                text: `${nombres} ${apellidos}`, value: idpersona                                
                            });
                        }
                    } else {
                        this.lista_voluntarios = [];                        
                    }
                } else {
                    this.lista_voluntarios = [];                    
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
                , voluntarios: this.voluntario
                , descripcion: this.descripcion.toUpperCase()
            }            
            try {
                const res  = await axios.post('/actividades/solicitud_hospital/nuevo_informe', this.dataEnvio);                                
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
                , voluntarios: this.voluntario
                , descripcion: this.descripcion.toUpperCase()
            }            
            try {
                const res  = await axios.put('/actividades/solicitud_hospital/modificar_informe', this.dataEnvio);                                
                if(res.data.estado==true) {
                    location.href = '/actividades/solicitud_hospital/informevisitas';
                }
            } catch (error) {
                console.error(error);
            }
        }
        , cargarFormulario: async function () {
            this.editar = true;
            const idlista = localStorage.getItem('idlista');
            try {
                const res = await axios.get(`/actividades/solicitud_hospital/get_informes/${idlista}`);               
                const data = await res.data;                                                 
                this.solicitudes = data.idlista;
                $('#solicitudes').val(data.idlista);
                $('#solicitudes').trigger('change');
                this.obtenerVoluntarios();   
                this.voluntario = data.idvoluntario;               
                $('#voluntario').val(data.idvoluntario);  
                $('#voluntario').trigger('change'); 
                this.descripcion = data.descripcion;                           
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