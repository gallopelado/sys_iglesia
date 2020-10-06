new Vue({
    delimiters: ['[[', ']]'],
    el:'#app',
    data: {
        modulos: null,
        paginas: null,
        lista_modulos: [],
        lista_paginas: []
    },
    methods: {
        getPagina() {
            if(this.modulos) {
                axios.get(`/mantenimiento_seguridad/permisos/get_pagina/${this.modulos}/${$("#gru_id").val()}`). then(({data}) => this.lista_paginas = data)
            } else {
                this.paginas = [];
            }
        }
    },
})