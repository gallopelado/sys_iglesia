/**
 * Fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramirez
 */

var app = new Vue({
    el: '#app'
    , data: {
        idmalla: sessionStorage.getItem('idmalla')
        , chk_habilita_area: false
        , cbo_area:''
        , cbo_curso:''
        , lista_areas: null
        , area_seleccionada: null
        , lista_cursos:[]
        , lista_tabla:[]
        , valido: 0
        , anho:''
        , anho_id:''
        , anio_des: parseInt(sessionStorage.getItem('anio_des'))
        , anho_etiqueta_tabla : parseInt(sessionStorage.getItem('anio_des'))
        , editar: sessionStorage.getItem('editar')
    }
    , methods: {
        habilitaArea: function () {
            this.valido = this.chk_habilita_area ? 0 : 1;
            this.cbo_area = this.chk_habilita_area ? '' : ''
            if(this.valido == 0)
                this.recargarCursos();
        }
        , obtenerAreaCursos: function() {
            const area = this.cbo_area;
            if(area) {
                const id = area.area_id;
                axios.get(`/cursos/malla_curricular/get_areacursos/${id}`)
                .then(res => {
                    this.lista_cursos = res.data;
                })
                .catch(e => {
                    console.error(e);
                })
            }
        }
        , recargarCursos: function () {
            axios
            .get(`/cursos/malla_curricular/get_cursos`)
            .then(res => {
                this.lista_cursos = res.data
            })
            .catch(error => {
                console.error(error);
            });
        }
        , verificaMallaAnho: function () {
            axios
            .get(`/cursos/malla_curricular/verifica_malla_anho`)
            .then(res => {
                this.anho = res.data.anho_des;
            })
            .catch(error => {
                console.error(error);
            });
        }
        //Verifica y llena la tabla de cursos del formulario
        , verificaExistenciaMallaCursos: function () {
            const idmalla = this.idmalla;
            if(idmalla) {
                axios
                .get(`/cursos/malla_curricular/get_cursosregistrados/${idmalla}`)
                .then(res => {
                    this.lista_tabla = res.data
                })
                .catch(error => {
                    console.error(error);
                });
            }
        }
        , validarMiniFormulario: function () {
            if(this.cbo_curso) {
                return true;
            } else {
                alert('Favor elija un curso');
                this.$refs.cbo_curso.focus();
                return false;
            }
        }
        , guardar: function () {
            if(this.validarMiniFormulario()) {
                const data = {
                    cur_id:this.cbo_curso.cur_id
                    , anho_id:this.anho_id
                }
                if(!this.idmalla) {
                    axios
                    .post(`/cursos/malla_curricular/guardar`, data)
                    .then(res => {
                        if(res.data.estado) {
                            this.verificaExistenciaMallaCursos();
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
                } else {
                    //actualizar cabecera
                    const data = {
                        malla_id: this.idmalla
                        , cur_id: this.cbo_curso.cur_id
                        , estado: true
                    }
                    axios
                    .put(`/cursos/malla_curricular/agregar_nuevos_cursos_malla`, data)
                    .then(res => {
                        if(res.data.estado) {
                            this.verificaExistenciaMallaCursos();
                        } else {
                            alert('El valor estar repetido');
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
                }
                
            }
        }
        , anularCursoMalla: function (cur_id) {
            const op = confirm('Desea anular este curso ?');
            if(op) {
                const data = {
                    malla_id: this.idmalla
                    , cur_id: cur_id
                    , estado: false
                }
                axios
                .put(`/cursos/malla_curricular/anular_curso_malla`, data)
                .then(res => {
                    if(res.data.estado) {
                        this.verificaExistenciaMallaCursos();
                    } else {
                        alert('Lo siento, hubo un error al intentar anular. Consulte con el Administrador del sistema');
                    }
                })
                .catch(error => {
                    console.error(error);
                });
            }
        }
        , detalleCurso: function (idmalla, cur_id, cur_des) {
            sessionStorage.setItem('cur_des', cur_des);
            location.href = `/cursos/malla_curricular/form_asignatura_malla_curricular/${idmalla}/${cur_id}`;
        }
    }
    , mounted() {
        axios
        .get(`/cursos/malla_curricular/get_areas`)
        .then(res => {
            this.lista_areas = res.data
        })
        .catch(error => {
            console.error(error);
        });

        axios
        .get(`/cursos/malla_curricular/get_cursos`)
        .then(res => {
            this.lista_cursos = res.data
        })
        .catch(error => {
            console.error(error);
        });

        axios
        .get(`/cursos/malla_curricular/get_anhohabil`)
        .then(res => {
            this.anho_id = res.data.anho_id
            this.anho = res.data.anho_des
        })
        .catch(error => {
            console.error(error);
        });

        this.verificaExistenciaMallaCursos();
    }
    , delimiters: ['[[',']]']
});