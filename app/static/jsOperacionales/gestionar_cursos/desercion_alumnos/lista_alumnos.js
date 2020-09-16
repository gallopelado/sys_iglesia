/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data: {
        curso: null,
        lista_alumnos: [],
        desercion_data: JSON.parse(sessionStorage.getItem('desercion_data'))
    },
    methods: {
        cargarCabecera() {
            this.curso = this.desercion_data.curso;
        },
        
        cargarListaAlumnos() {
            const { cur_id } = this.desercion_data;
            axios.get(`/cursos/desercion_alumnos/get_cursos_inscriptos/${cur_id}`).then(({ data }) => this.lista_alumnos = data)
        },

        escogerAlumno(item) {
            console.log(item);
        }
    },
    mounted() {
        this.cargarCabecera();
        this.cargarListaAlumnos();
    },
})