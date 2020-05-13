var app = new Vue({
    el: '#app'
    , data: {
        curso: sessionStorage.getItem('cur_des')
        , cbo_asignatura:''
        , lista_asignaturas:[]
        , h_catedra:null
        , lista_tabla_asignaturas:[]
        , idmalla: sessionStorage.getItem('idmalla')
        , cur_id: sessionStorage.getItem('cur_id')
    }
    , methods: {
        obtenerAsignaturasCurso() {
            const idmalla = this.idmalla;
            const cur_id = this.cur_id;
            axios
            .get(`/cursos/malla_curricular/get_asignaturascurso/${idmalla}/${cur_id}`)
            .then(res => {
                this.lista_tabla_asignaturas = res.data
            })
            .catch(error => {
                console.error(error);
            });
        }
        , obtenerTodasAsignaturas() {
            axios
            .get(`/cursos/malla_curricular/get_todas_asignaturas`)
            .then(res => {
                this.lista_asignaturas = res.data
            })
            .catch(error => {
                console.error(error);
            });
        }
        , guardarAsignatura() {
            if(!this.cbo_asignatura) {
                alert('No debe estar vacia la asignatura');
                this.$refs.cbo_asignatura.focus();
                return;
            }
            if(this.h_catedra < 0 || !this.h_catedra) {
                alert('No pueder ser menor');
                this.$refs.h_catedra.focus();
                return;
            }
            const data = {
                malla_id: this.idmalla, 
                cur_id: this.cur_id,
                asi_id: this.cbo_asignatura.asi_id,
                num_id:this.cbo_asignatura.num_id, 
                cant_horas: this.h_catedra
            }
            console.log(data);
            axios
            .post(`/cursos/malla_curricular/agregar_nuevos_asignatura`, data)
            .then(res => {
                if(res.data.estado) {
                    this.obtenerAsignaturasCurso();
                    this.cbo_asignatura = null;
                    this.h_catedra = null
                } else {
                    alert('El valor estar repetido');
                }
            })
            .catch(error => {
                console.error(error);
            });
        }
    }
    , mounted() {
        this.obtenerAsignaturasCurso();
        this.obtenerTodasAsignaturas();
    }
    , delimiters: ['[[',']]']
})