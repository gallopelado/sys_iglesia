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
    }
    , beforeMount() {
        this.obtenerLista();
    }
    , delimiters: ['[[',']]']
})