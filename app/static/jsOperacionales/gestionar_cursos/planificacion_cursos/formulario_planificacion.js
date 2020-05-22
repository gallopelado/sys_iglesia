/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el: '#app'
    , data: {
        editar: sessionStorage.getItem('editar')
        , idmalla: sessionStorage.getItem('idmalla')
        , fecha_malla: sessionStorage.getItem('fecharegistro')
        , cbo_curso: null
        , cbo_asignatura: null
        , cbo_maestro: null
        , cbo_turno: null
        , fecha_inicio: null
        , fecha_fin: null
        , lista_cursos: []
        , lista_asignaturas: []
        , lista_maestros: []
        , lista_turnos: ['MAÑANA', 'TARDE', 'NOCHE']
        , det_asignaturas: []
    }
    , methods: {
        getDetalleAsignaturas() {
            const idplan = this.idmalla;
            const idcurso = this.cbo_curso.cur_id;
            if(idcurso) {
                //Obtener detalle del backend
                axios
                .get(`/cursos/planificacion_cursos/get_detalle_asignaturas/${idplan}/${idcurso}`)
                .then(res => {
                    console.log(res);
                    this.det_asignaturas = res.data
                })
                .catch(error => {
                    console.error(error);
                });
            } else {
                this.det_asignaturas = [];
            }
        }
    },
    mounted() {
        //Carga de combo cursos
        axios
            .get(`/cursos/malla_curricular/get_cursos`)
            .then(res => {
                this.lista_cursos = res.data
            })
            .catch(error => {
                console.error(error);
            });

        //Carga de asignaturas
        axios
            .get(`/cursos/malla_curricular/get_todas_asignaturas`)
            .then(res => {
                this.lista_asignaturas = res.data
            })
            .catch(error => {
                console.error(error);
            });

        //Carga de maestros
        axios
            .get(`/cursos/planificacion_cursos/get_maestros`)
            .then(res => {
                this.lista_maestros = res.data
            })
            .catch(error => {
                console.error(error);
            });
    }
    , delimiters: ['[[', ']]']
});
