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
        , idmalla: 2
        , idmaestro: 2
        , turno: 'NOCHE'
    }
    , methods: {
        listarClasesMaestro() {
            axios.get(`/cursos/asistencia_alumnos/lista_profesor_cursos_asignatura/${this.idmalla}/${this.turno}/${this.idmaestro}`)
            .then(res => {
                this.lista_asistencias = res.data;
            })
            .catch(error => {
                console.error(error);
            })
        }
        , formatearTabla() {
            $('#tabla_curso').DataTable({
                "language": idioma_spanish
            });
        }
    }
    , mounted() {
        this.listarClasesMaestro();
    }
    , updated() {
        this.formatearTabla();
    }
    , delimiters: ['[[', ']]']
});