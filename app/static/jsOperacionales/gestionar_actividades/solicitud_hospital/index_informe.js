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
            /*try {
                const res = await axios.get('/actividades/solicitud_hospital/obtener_lista_voluntarios');                
                this.lista = await res.data;                    
            } catch (error) {
                console.error(error);
            }*/
            this.lista = 0;
        }
        , modificar: function (id) {
            const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
            m.buttons.Si.action = () => {                
                location.href = `/actividades/solicitud_hospital/modificar_voluntarios/${id}`;                
            }
            m.open();
        }
        , ver: function (id) {               
            location.href = `/actividades/solicitud_hospital/ver_voluntarios/${id}`;                
        }
        , eliminar: async function(id) {
            const m = confirm('Desea eliminar?');
            if(m) {
                try {
                    const datos = {idsolicitud: id};
                    const res = await axios.put('/actividades/solicitud_hospital/baja_lista_voluntario', datos);
                    if(res.data.estado==true) {
                        location.href = '/actividades/solicitud_hospital/voluntarios';
                    }
                } catch (error) {
                    console.error(error);
                }
            }              
        }
    }
    , beforeMount() {
        this.obtenerLista();
    }
    , delimiters: ['[[',']]']
})