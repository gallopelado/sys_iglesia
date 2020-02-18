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
                const res = await axios.get('/actividades/solicitud_hospital/obtener_lista_voluntarios');
                console.log(res);
                this.lista = await res.data;                    
            } catch (error) {
                console.error(error);
            }
        }
        , modificar: function (id) {
            const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
            m.buttons.Si.action = () => {                
                location.href = `/actividades/solicitud_hospital/modificar_voluntarios/${id}`;                
            }
            m.open();
        }
    }
    , beforeMount() {
        this.obtenerLista();
    }
    , delimiters: ['[[',']]']
})