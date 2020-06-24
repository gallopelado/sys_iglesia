/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el:'#app'
    , data: {
        pre_data: JSON.parse(sessionStorage.getItem('alumno_data'))
        , alumno: null
        , cbo_turno: null
        , malla_id: null
        , cur_id: null
        , curso: null
        , cbo_asignatura: null
        , lista_asignaturas: null
        , lista_asignatura_alumno: null
        , lista_alumnos: []
        , det_alumnos: []
        , btn_agregar_estado: false 
    }
    , methods: {
        listaAsignaturas() {
            const malla_id = this.pre_data.malla_id;
            const curso_id = this.pre_data.cur_id;
            axios
            .get(`/cursos/inscripcion_alumnos/get_asignaturas/${malla_id}/${curso_id}`)
            .then(res => {
                this.lista_asignaturas = res.data;
            })
            .catch(error => {
                console.error(error);
            });
        }
        , listaAsignaturasAlumno() {
            const malla_id = this.pre_data.malla_id;
            const curso_id = this.pre_data.cur_id;
            const per_id = this.pre_data.per_id;
            
            axios
            .get(`/cursos/inscripcion_alumnos/get_asignaturas_alumno/${malla_id}/${curso_id}/${per_id}`)
            .then(res => {                
                this.lista_asignatura_alumno = res.data;
            })
            .catch(error => {
                console.error(error);
            });
        }
        , listaPersonas() {
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
        , editarAsignaturas(alumno) {
            sessionStorage.setItem('alumno_data', JSON.stringify(alumno));
            location.href = '/cursos/inscripcion_alumnos/form_asignatura';
        }
    }
    , mounted() {
        this.alumno = `${this.pre_data.per_nombres} ${this.pre_data.per_apellidos}`;
        this.curso = this.pre_data.nombre_curso;
        this.listaAsignaturas();
        this.listaAsignaturasAlumno();
    }
    , delimiters: ['[[', ']]']
}) 