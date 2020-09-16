/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        malla_id: null,
        cur_id: null,
        per_id: null,
        curso: null,
        alumno: null,
        motivo_desercion: null,
        descripcion: null,
        lista_motivo_desercion: [],
        alumnoSeleccionado: JSON.parse(sessionStorage.getItem('alumno_seleccionado'))
    },
    methods: {
        cargarFormulario() {
            this.malla_id = this.alumnoSeleccionado.malla_id;
            this.cur_id = this.alumnoSeleccionado.cur_id;
            this.per_id = this.alumnoSeleccionado.per_id;
            this.curso = this.alumnoSeleccionado.curso;
            this.alumno = this.alumnoSeleccionado.alumno;
        },

        getMotivoDesercion() {
            axios.get(`/cursos/desercion_alumnos/get_motivo_desercion`).then(({data}) => this.lista_motivo_desercion= data)
        }
    },
    mounted() {
        this.cargarFormulario();
        this.getMotivoDesercion();
    },
})