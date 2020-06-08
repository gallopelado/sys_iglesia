/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el:'#app'
    , data: {
        pre_data: JSON.parse(sessionStorage.getItem('pre_data'))
        , malla_id: null
        , cur_id: null
        , curso: null
        , cbo_alumno: null
        , lista_alumnos: []
        , det_alumnos: []
    }
    , methods: {
        listaPersonas() {
            axios
            .get(`/cursos/inscripcion_alumnos/get_personas`)
            .then(res => {
                this.lista_alumnos = res.data;
            })
            .catch(error => {
                console.error(error);
            });
        }
    }
    , mounted() {
        this.curso = this.pre_data.curso;
        this.malla_id = this.pre_data.malla_id;
        this.cur_id = this.pre_data.cur_id;
        this.listaPersonas();
    }
    , delimiters: ['[[', ']]']
}) 