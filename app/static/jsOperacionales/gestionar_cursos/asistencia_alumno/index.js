import { idioma_spanish } from '../../helper/helper.js';
/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */
var app = new Vue({
    el:'#app'
    , data: {
        lista_asistencias: []
        , lista_cursos: null
        , lista_asignaturas: null
        , idmalla: $('#malla_id').val()
        , idmaestro: $('#fun_id').val()
        , turno: 'NOCHE'
        , lista_turnos: ['MAÑANA', 'TARDE', 'NOCHE']
        , cbo_turno: null
        , cbo_curso: null
        , cbo_asignatura: null
    }
    , methods: {
        listarClasesMaestro() {
            const cbo_turno = !this.cbo_turno ? 'NOCHE': this.cbo_turno;
            const cbo_curso = !this.cbo_curso ? '1' : this.cbo_curso.cur_id;
            const cbo_asignatura = !this.cbo_asignatura ? '1' : this.cbo_asignatura;
            const num_id = !this.cbo_asignatura ? '1' : this.cbo_asignatura.num_id;
            axios.get(`/cursos/asistencia_alumnos/lista_profesor_cursos_asignatura/${this.idmalla}/${cbo_turno}/${this.idmaestro}/${cbo_curso}/${cbo_asignatura.asi_id}/${num_id}`)
            .then(res => {
                if(res.data.codigo) {
                    this.lista_asistencias = [];
                } else {
                    this.lista_asistencias = res.data;
                }
            })
            .catch(error => {
                console.error(error);
            })
        }
        , listarCursos() {
            axios.get(`/cursos/asistencia_alumnos/lista_cursos_maestro/${this.idmalla}/${this.idmaestro}`)
            .then(res => {
                this.lista_cursos = res.data;
            })
            .catch(error => {
                console.log(error);
            })
        }
        , listarAsignaturasPorCurso() {
            axios.get(`/cursos/asistencia_alumnos/lista_asignatura_maestro/${this.idmalla}/${this.idmaestro}/${this.cbo_curso.cur_id}`)
            .then(res => {
                this.lista_asignaturas = res.data;
            })
            .catch(error => {
                console.log(error);
            })
        }
        , cargarAsistencia(item) {
            if(item) {
                item.turno = this.turno;
                sessionStorage.setItem('asistencia_data', JSON.stringify(item));
                location.href = `/cursos/asistencia_alumnos/form_asistencia`;
            }
        }
        , formatearTabla() {
            let dtclases = $("#tabla_curso");
            if ($.fn.dataTable.isDataTable('#tabla_curso')) {
                dtclases.DataTable().destroy();
            }
            //this.listarClasesMaestro();
            $('#tabla_curso').DataTable({
                "language": idioma_spanish
            });
        }
    }
    , beforeCreate() {
        //this.listarClasesMaestro();
        //this.formatearTabla();
    }
    , created() {
        //this.formatearTabla();
        //this.listarClasesMaestro();
    }
    , beforeMount() {
        //this.listarClasesMaestro();
        //this.formatearTabla();
    }
    , mounted() {
       this.listarClasesMaestro();
       this.listarCursos();
       //this.formatearTabla();
    } , beforeUpdate() {
        //this.formatearTabla();
    }
    , updated() {
        //this.formatearTabla();
        //this.listarClasesMaestro();
    }
    
    , delimiters: ['[[', ']]']
});