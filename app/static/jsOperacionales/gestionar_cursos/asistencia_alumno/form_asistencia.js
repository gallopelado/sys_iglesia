/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */
var app = new Vue({
    el:'#app'
    , data: {
        asistencia_data: JSON.parse(sessionStorage.getItem('asistencia_data'))
        , materia: null
        , curso: null
        , turno: null
        , descripcion: null
        , det_alumnos: null
        , fecha_clase: null
        , asistio: null
        , puntual: null
        , lista_asistio: [], lista_puntual: [], lista_ausente:[]
        , formulario_data: []
        , guardado: false
    }
    , methods: {
        cargarFormulario() {
            if(this.formulario_data.length == 0) {
                $.dialog({
                    title: 'Atención!',
                    content: 'Todavia no se ha registrado asistencia!',
                });
            }
        }
        , getListaAlumnos() {
            const { malla_id, cur_id, asi_id, num_id, turno } = this.asistencia_data;
            axios.get(`/cursos/asistencia_alumnos/lista_alumnos_curso/${malla_id}/${cur_id}/${asi_id}/${num_id}/${turno}`)
            .then(res => {
                this.det_alumnos = res.data;
            })
            .catch(error => {
                console.error(error);
            })
        }
        , getDatosFormulario() {
            //malla_id, asi_id, num_id, per_id, turno, cur_id, fechaclase
            const {malla_id, asi_id, num_id, per_id, turno, cur_id, fecha} = this.asistencia_data;
            axios.get(`/cursos/asistencia_alumnos/get_formulario_asistencia/${malla_id}/${asi_id}/${num_id}/${per_id}/${turno}/${cur_id}/${fecha}`)
            .then(res => {
                this.formulario_data = res.data;
                this.cargarFormulario();
            })
            .catch(error => {
                console.error(error);
            })
        }
        , agregaAsistencia(data) {
            this.lista_asistio = [];
            this.lista_ausente = [];
            let item = this.$refs.chk_asistio;
            for (let i = 0; i < item.length; i++) {
                if (item[i].checked) {
                    this.$refs.chk_puntual[i].disabled = false;
                    this.lista_asistio.push({
                        idalumno: item[i].id
                    });
                } else {
                    this.lista_ausente.push({
                        idalumno: item[i].id
                    });
                    this.lista_puntual = [];
                    this.$refs.chk_puntual[i].checked = false;
                    this.$refs.chk_puntual[i].disabled = true;
                }
            }
        }
        , agregaPuntualidad(data) {
            this.lista_puntual = [];
            let item = this.$refs.chk_puntual;
            for (let i = 0; i < item.length; i++) {
                if (item[i].checked) {
                    this.lista_puntual.push({
                        idalumno: item[i].id
                    });
                }
            }
        }
        , guardar() {
            const inst = this;
            $.confirm({
                theme: 'supervan',
                title: 'Atención',
                content: 'Está seguro de guardar las asistencias?',
                buttons: {
                    Si: {
                        text: 'Si',
                        btnClass: 'btn-blue',                
                        action: function(){
                            const form = {
                                malla_id: inst.asistencia_data.malla_id
                                , asi_id: inst.asistencia_data.asi_id
                                , num_id: inst.asistencia_data.num_id
                                , per_id: inst.asistencia_data.per_id
                                , turno: inst.asistencia_data.turno
                                , cur_id: inst.asistencia_data.cur_id, descripcion: inst.descripcion
                                , asistieron: inst.lista_asistio, puntuales: inst.lista_puntual, ausentes: inst.lista_ausente
                                , fecha: inst.asistencia_data.fecha
                            }
                            axios.post(`/cursos/asistencia_alumnos/guardar_asistencia`, form)
                            .then(res => {
                                if(res.data.cabecera_id) {
                                    $.dialog({
                                        title: 'Correcto',
                                        content: 'Se registro exitosamente',
                                        onOpen: function () {
                                            inst.guardado = true;
                                        }
                                    });
                                } else if(res.data.cod === '001') {
                                    $.dialog({
                                        title: 'Fecha no valida',
                                        content: res.data.mensaje,
                                    });
                                } else if(res.data.cod === '002') {
                                    $.dialog({
                                        title: 'Fecha no valida',
                                        content: res.data.mensaje,
                                    });
                                }
                            })
                            .catch(error => {
                                console.error(error);
                            })
                        }
                    },
                    No: {
                        text: 'No',
                        btnClass: 'btn-red',                
                        action: function(){
                            
                        }
                    }
                }
            });
        }
    }
    , mounted() {
        this.materia =  `${this.asistencia_data.asi_des} ${this.asistencia_data.num_des}`;
        this.curso =  this.asistencia_data.cur_des;
        this.turno =  this.asistencia_data.turno;
        this.fecha_clase = this.asistencia_data.fecha_larga;
        this.getDatosFormulario();
        this.getListaAlumnos();
    }
    , delimiters: ['[[', ']]']
});