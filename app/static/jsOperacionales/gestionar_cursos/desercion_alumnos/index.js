/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data: {
        lista_cursos: null,
        lista_maestros: [],
        lista_turnos: ['MAÑANA', 'TARDE', 'NOCHE'],
        cbo_maestro: null,
        cbo_turno: null
    },
    methods: {
        getMaestros() {
            axios.get(`/cursos/desercion_alumnos/get_maestros`).then(({ data }) => this.lista_maestros=data)
        },
        
        getCursoMaestro() {
            const inst = this
            const maestro = this.cbo_maestro ? this.cbo_maestro.per_id : null;
            const turno = this.cbo_turno;
           if(maestro && turno) {
                axios.get(`/cursos/desercion_alumnos/get_curso_maestro/${maestro}/${turno}`).then(({data}) => {
                    inst.lista_cursos = data;
                    console.log(data);
               })
           } else {
            $.alert({
                title: 'Cuidado!',
                content: 'Debe seleccionar ambas opciones!',
                onClose: function () {
                    // before the modal is hidden.
                   $('#cbo_turno').click()
                }
            });
           }
        }

    },
    mounted() {
        this.getMaestros();
        //this.getCursoMaestro();
    },
})