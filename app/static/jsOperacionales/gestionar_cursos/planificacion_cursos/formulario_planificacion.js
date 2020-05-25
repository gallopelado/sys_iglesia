/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

var app = new Vue({
    el: '#app'
    , data: {
        editar: sessionStorage.getItem('editar')=='false'?false:true
        , idmalla: sessionStorage.getItem('idmalla')
        , anio_des: parseInt(sessionStorage.getItem('anio_des'))
        , fecha_actual: null
        , fecha_malla: sessionStorage.getItem('fecharegistro')
        , cbo_curso: null
        , cbo_asignatura: null
        , cbo_maestro: null
        , cbo_turno: null
        , fecha_inicio: null
        , fecha_fin: null
        , fecha_max:null
        , lista_cursos: []
        , lista_asignaturas: []
        , lista_maestros: []
        , lista_turnos: ['MAÑANA', 'TARDE', 'NOCHE']
        , det_asignaturas: []
        , desactivar_boton_asignatura: true
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
                    this.det_asignaturas = res.data
                })
                .catch(error => {
                    console.error(error);
                });
            } else {
                this.det_asignaturas = [];
            }
        }
        , agregarCurso() {
            if(this.cbo_curso) {
                const data = {
                    malla_id:this.idmalla, cur_id:this.cbo_curso.cur_id
                }
                axios
                    .post(`/cursos/planificacion_cursos/agregar_curso`, data)
                    .then(res => {                
                        if(res.data.codigo == '23505') {
                            $.alert('Este curso ya esta registrado o desactivado!');
                        } else if(res.data.nrofilas > 0) {
                            $.alert('Esta operacion fue exitosa!');
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            } else {
                $.alert({
                    title: 'Cuidado!',
                    content: 'Debe escoger un curso',                    
                });
            }
        }
        , agregarAsignatura() {
            if(this.validarCombos() && this.validarFechas()) {
                const data = {
                    malla_id: this.idmalla
                    , cur_id: this.cbo_curso.cur_id
                    , asi_id: this.cbo_asignatura.asi_id
                    , num_id: this.cbo_asignatura.num_id
                    , per_id: this.cbo_maestro.per_id
                    , turno: this.cbo_turno
                    , fecha_inicio: this.fecha_inicio
                    , fecha_fin: this.fecha_fin
                }
                axios
                    .post(`/cursos/planificacion_cursos/agregar_asignatura`, data)
                    .then(res => {                
                        if(res.data.codigo == '23505') {
                            $.alert('Esta asignatura ya esta registrado o desactivado!');
                        } else if(res.data.nrofilas > 0) {
                            $.alert('Esta operacion fue exitosa!');
                            this.getDetalleAsignaturas();
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            }
        }

        , anularAsignatura(item) {
            const op = confirm('Dese anular este curso ?');
            if(op) {
                const data = {
                    //malla_id, asi_id, num_id, per_id, turno, cur_id
                    malla_id: item.malla_id, asi_id: item.asi_id, num_id: item.num_id
                    , per_id: item.idmaestro, turno: item.turno, cur_id: item.cur_id
                }
                axios
                .put(`/cursos/planificacion_cursos/anular_asignatura`, data)
                .then(res => {                
                    if(res.data.codigo == '23505') {
                        $.alert('Esta asignatura ya esta registrado o desactivado!');
                    } else if(res.data.nrofilas > 0) {
                        $.alert('Esta operacion fue exitosa!');
                        this.getDetalleAsignaturas();
                    }
                })
                .catch(error => {
                    console.error(error);
                });
            }
        }

        , validarFechas() {
            const anio_des = this.anio_des;
            const fecha_inicio = new Date(this.fecha_inicio);
            const fecha_fin = new Date(this.fecha_fin);
            if(fecha_fin >= fecha_inicio) {                
                return true;
            } else {
                $.alert('Las fechas ingresadas no son correctas');
                return false;
            }
        }
        , validarCombos() {
            if(this.cbo_asignatura && this.cbo_maestro && this.cbo_turno) {
                return true;
            } else {
                $.alert('Por favor verifique alguna de las opciones, no deben quedar vacias');
                return false;
            }
        }
        , detalleAsignatura(item) {
            console.log(item);
            sessionStorage.setItem('asignatura_data', JSON.stringify(item));
            location.href = `/cursos/planificacion_cursos/form_frecuencia_asignatura`;
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
        
        //Carga fecha actual
        axios
            .get(`/cursos/planificacion_cursos/get_fecha_actual`)
            .then(res => {
                this.fecha_actual = res.data.fecha_actual;
                this.fecha_inicio = this.fecha_actual;
                this.fecha_fin = this.fecha_actual;
                this.fecha_max = moment(new Date(this.anio_des, 11, 31)).format('YYYY-MM-DD') 
            })
            .catch(error => {
                console.error(error);
            });
    }
    , delimiters: ['[[', ']]']
});
