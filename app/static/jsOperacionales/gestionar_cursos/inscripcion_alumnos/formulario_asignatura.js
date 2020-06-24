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
        
        , agregarAsignaturaAlumno() {
            //asignatura['malla_id'], asignatura['curso_id'], asignatura['per_id'], asignatura['asi_id'], asignatura['num_id'], asignatura['turno']
            const asignatura = {
                malla_id: this.pre_data.malla_id, curso_id: this.pre_data.cur_id, per_id: this.pre_data.per_id
                , turno: this.cbo_turno, asi_id: this.cbo_asignatura.asi_id, num_id: this.cbo_asignatura.num_id
            }
            axios.post(`/cursos/inscripcion_alumnos/guardar_asignatura_alumno`, asignatura)
                .then(res => {
                    if (res.data.codigo == '23505') {
                        $.alert('Esta asignatura ya esta registrada !');
                    } else if (res.data.nrofilas > 0) {
                        $.alert('Esta operacion fue exitosa!');
                        this.listaAsignaturasAlumno();
                    }
        })
        .catch(error => {
            console.error(error);
        });
        }
        , anularAsignaturaAlumno(item) {
            const asignatura = {
                malla_id: item.malla_id, curso_id: item.cur_id, per_id: item.per_id
                , turno: item.turno, asi_id: item.asi_id, num_id: item.num_id
            }
            axios.put(`/cursos/inscripcion_alumnos/anular_asignatura_alumno`, asignatura)
            .then(res => {
                if (res.data.codigo == '23505') {
                    $.alert('Esta asignatura ya esta registrada !');
                } else if (res.data.nrofilas > 0) {
                    $.alert('Esta operacion fue exitosa!');
                    this.listaAsignaturasAlumno();
                }
            })
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