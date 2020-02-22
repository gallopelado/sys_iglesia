import { idioma_spanish, mensajeConfirmacion } from '../../helper/helper.js';
var app =  new Vue({
    el:'#app'
    , data: {
        idsolicitud:''
        , solicitud:''
        , fechavisita:''
        , estado:''
        , lista:[]
    }
    , methods: {
        obtenerLista: async function() {
            try {
                const res = await axios.get('/actividades/solicitud_hospital/get_informes');                
                this.lista = await res.data;                    
            } catch (error) {
                console.error(error);
            }            
        }
        , modificar: function (id) {
            const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
            m.buttons.Si.action = () => {                
                location.href = `/actividades/solicitud_hospital/editar_informe/${id}`;                
            }
            m.open();
        }
        , ver: function (id) {               
            location.href = `/actividades/solicitud_hospital/ver_informe/${id}`;                
        }
    }
    , beforeMount() {
        this.obtenerLista();
    }
    , delimiters: ['[[',']]']
})