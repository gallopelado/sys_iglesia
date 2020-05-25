var app = new Vue({
    el:'#app'
    , data: {
        data_asignatura:JSON.parse(sessionStorage.getItem('asignatura_data'))
        , idmalla:null
        , cur_des:null
        , per_des:null
        , asi_des:null
        , turno:null        
        , hora_inicio:null
        , hora_fin:null
        , hora_min:'06:00'
        , hora_max:'21:00'
        , cbo_dia:[]
        , lista_dias:['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO']
        , det_asignaturas:[]
    }
    , methods: {
        cargarFormulario() {
            const {
                asi_des, asi_id, num_id, num_des, cur_des, cur_id, turno
                , idmaestro, per_nombres, per_apellidos, malla_id
            } = this.data_asignatura;
            this.cur_des = cur_des;
            this.per_des = `${per_nombres} ${per_apellidos}`;
            this.asi_des = `${asi_des} ${num_des}`;
            this.turno = turno;
            this.idmalla = malla_id
        }
        , agregarHorario() {
            let data = {};
            if(this.cbo_dia == '') {                
                $.alert('Debe elegir un dia');                
                this.$refs.cbo_dia.focus();
                return;         
            }
            if(this.cbo_dia && this.validarHoras()) {
                data = {
                    malla_id: this.idmalla
                    ,asi_id: this.data_asignatura.asi_id
                    ,num_id: this.data_asignatura.num_id
                    ,per_id: this.data_asignatura.idmaestro
                    ,cur_id:  this.data_asignatura.cur_id
                    ,turno: this.turno
                    , dia: this.cbo_dia
                    , hora_inicio: this.hora_inicio
                    , hora_fin: this.hora_fin
                }
                console.log(data);
                axios
                    .post(`/cursos/planificacion_cursos/agregar_horario_asignatura`, data)
                    .then(res => {                
                        this.det_asignaturas = res.data;
                        if(res.data.codigo == '23505') {
                            $.alert('Esto ya esta registrado!');
                        } else if(res.data.nrofilas > 0) {
                            $.alert('Esta operacion fue exitosa!');
                            this.getDetalleFrecuencia();
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            } 
        }
        , eliminarHorario(item) {
            let data = {
                "id":item.frma_id
            };
            axios
                .post(`/cursos/planificacion_cursos/eliminar_horario_asignatura`, data)
                .then(res => {                
                    this.det_asignaturas = res.data;
                    if(res.data.codigo == '23505') {
                        $.alert('Esto ya esta registrado!');
                    } else if(res.data.nrofilas > 0) {
                        $.alert('Esta operacion fue exitosa!');
                        this.getDetalleFrecuencia();
                    }
                })
                .catch(error => {
                    console.error(error);
                });
        }
        , validarHoras() {
            //const inst = this;
            const hora_inicio = moment(this.hora_inicio+":00", 'hh:mm');
            const hora_fin = moment(this.hora_fin+":00", 'hh:mm');            
            const data = this.det_asignaturas;
            let data_filtrada1 = data.filter(item => hora_inicio.isBetween( moment((item.frma_horainicio+":00"),'hh:mm'), moment((item.frma_horafin+":00"),'hh:mm'), 'minutes', '[]' ) && item.frma_dia==this.cbo_dia);
            let data_filtrada2 = data.filter(item => hora_fin.isBetween( moment((item.frma_horainicio+":00"),'hh:mm'), moment((item.frma_horafin+":00"),'hh:mm'), 'minutes', '[]' )&& item.frma_dia==this.cbo_dia);            
            if(data_filtrada1.length != 0 || data_filtrada2.length != 0) {
                $.alert('Las horas ya existen, favor revise');
                return false;
            } else if(this.hora_fin > this.hora_inicio) {
                return true;            
            } else {
                $.alert('Las horas no son correctas, favor revise');
                return false;
            }            
        }
        , getDetalleFrecuencia() {
            //malla_id, asi_id, num_id, per_id, cur_id, turno
            const mall_id = this.idmalla;
            const asi_id = this.data_asignatura.asi_id;
            const num_id = this.data_asignatura.num_id;
            const per_id = this.data_asignatura.idmaestro;
            const cur_id =  this.data_asignatura.cur_id;
            const turno = this.turno;
            axios
                .get(`/cursos/planificacion_cursos/get_detalle_frecuencia/${mall_id}/${asi_id}/${num_id}/${per_id}/${cur_id}/${turno}`)
                .then(res => {                
                    this.det_asignaturas = res.data;
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
    , mounted() {
        this.cargarFormulario();
        this.getDetalleFrecuencia();
    }
    , delimiters: ['[[', ']]']
});