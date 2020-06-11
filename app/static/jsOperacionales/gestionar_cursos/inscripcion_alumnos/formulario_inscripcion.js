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
        , btn_agregar_estado: false 
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
        , getDetalleAlumnos() {            
            axios
            .get(`/cursos/inscripcion_alumnos/get_lista_alumnos_registrados/${this.malla_id}/${this.cur_id}`)
            .then(res => {
                this.det_alumnos = res.data;
            })
            .catch(error => {
                console.error(error);
            });
        }
        , inscribirAlumnoCurso() {
            //alumno['malla_id'], alumno['curso_id'], alumno['per_id']
            if(this.cbo_alumno) {
                const alumno = {
                    malla_id: this.malla_id, curso_id: this.cur_id, per_id: this.cbo_alumno.per_id
                }
                axios.post(`/cursos/inscripcion_alumnos/inscribir_alumno`, alumno)
                .then(res => {
                    if(res.data.codigo == '23505') {
                        $.alert('Esta persona ya esta registrada o desactivada!');
                    } else if(res.data.nrofilas > 0) {
                        $.alert('Esta operacion fue exitosa!');
                        this.getDetalleAlumnos();
                    }
                })
                .catch(error => {
                    console.error(error);
                });
            } else {
                alert('Debe escoger un alumno');
            }            
        }
        , actualizarEstadoInscripcionAlumno(id) {
            const alumno = {
                malla_id: this.malla_id, curso_id: this.cur_id, per_id: id
            }
            axios.put(`/cursos/inscripcion_alumnos/actualizar_estado_inscripcion_alumno`, alumno)
                .then(res => {
                    if (res.data.codigo == '23505') {
                        $.alert('Esta persona ya esta registrada o desactivada!');
                    } else if (res.data.nrofilas > 0) {
                        $.alert('Esta operacion fue exitosa!');
                        this.getDetalleAlumnos();
                    }
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
        this.getDetalleAlumnos();
    }
    , delimiters: ['[[', ']]']
}) 