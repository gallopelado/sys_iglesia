/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data: {
        lista_cursos: []
    },
    methods: {
        
        getCursosInscriptos() {
            const maestro = this.cbo_maestro ? this.cbo_maestro.per_id : null;
            const turno = this.cbo_turno;
            axios.get(`/cursos/desercion_alumnos/get_cursos_inscriptos`).then(({data}) => this.lista_cursos = data)
        },

        cargarDesercion(item) {
            if(item) {
                sessionStorage.setItem('desercion_data', JSON.stringify(item));
                location.href = `/cursos/desercion_alumnos/lista_alumnos`;
            }
        }

    },
    mounted() {
        this.getCursosInscriptos();
    },
})