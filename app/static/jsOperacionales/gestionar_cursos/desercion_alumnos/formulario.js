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
        },

        registrarDesercion() {
            const descripcion = this.descripcion && this.descripcion;
            if(this.motivo_desercion && this.descripcion.trim()) {
                const enviar = {
                    malla_id: this.malla_id, cur_id: this.cur_id, per_id: this.per_id, motivo_desercion: this.motivo_desercion.id, descripcion: this.descripcion
                }
                axios.post(`/cursos/desercion_alumnos/registrar_desercion`, enviar).then(({data}) => data.exitoso && history.back());
                return;
            }
            $.alert({
                title: 'Completar!',
                content: 'Favor complete el formulario antes de guardar!'
            });
        }
    },
    mounted() {
        this.cargarFormulario();
        this.getMotivoDesercion();
    },
})