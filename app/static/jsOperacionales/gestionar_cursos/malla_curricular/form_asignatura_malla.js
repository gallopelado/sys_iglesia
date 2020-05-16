var data = {
    curso: sessionStorage.getItem('cur_des')
    , cbo_asignatura:''
    , lista_asignaturas:[]
    , h_catedra:null
    , lista_tabla_asignaturas:[]
    , idmalla: sessionStorage.getItem('idmalla')
    , cur_id: sessionStorage.getItem('cur_id')
    , m_catedra: null
    , m_asignatura: null
    , m_id_asignatura: null
    , m_num_id: null
}

Vue.component('modal-editar_horas-catedra', {
    template: `
    <div class="modal fade" id="modal-editar_horas-catedra" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Modificar horas cátedra</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form>
                        <!--Asignatura, horas catedra-->
                        <div class="form-group row">
                            <label for="m_asignatura" class="col-sm-4 col-form-label">Asignatura</label>
                            <div class="col-8">
                                <div class="col-sm-12">
                                <input type="text" id="m_asignatura" name="m_asignatura" class="form-control form-control-sm" v-model="m_asignatura" disabled>
                                </div>                                    
                            </div>
                        </div>
                        
                        <div class="form-group row">
                            <label for="m_catedra" class="col-sm-4 col-form-label">Horas cátedra</label>
                            <div class="col-5">
                                <div class="col-sm-7">
                                <input type="number" class="form-control form-control-sm" id="m_catedra" ref="m_catedra" name="m_catedra" v-model="m_catedra" @keyup.enter="modificarAsignatura">
                                </div>                                    
                            </div>
                        </div>
                        <!---->
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                    <button type="button" class="btn btn-primary" @click="modificarAsignatura">Modificar</button>
                </div>
            </div>
        </div>
    </div>
    `
    , data: function () {
        return data;
    }
    , methods: {
        modificarAsignatura() {
            const data = {
                malla_id: this.idmalla, 
                cur_id: this.cur_id,
                asi_id: this.m_id_asignatura,
                num_id:this.m_num_id, 
                cant_horas: this.m_catedra
            }
            if(this.m_catedra < 0 || !this.m_catedra) {
                alert('No debe estar vacio la hora catedra ni ser negativo!');
                return;
            }
           
            axios
            .post(`/cursos/malla_curricular/agregar_nuevos_asignatura`, data)
            .then(res => {
                if(res.data.estado) {
                    app.obtenerAsignaturasCurso();
                    this.m_asignatura = null;
                    this.m_catedra = null
                    $('#modal-editar_horas-catedra').modal('toggle');
                    $.alert({
                        title: 'Éxito',
                        content: 'Se procesó correctamente!',
                        theme:'material'
                    });
                } else {
                    alert('El valor estar repetido');
                }
            })
            .catch(error => {
                console.error(error);
            });
        }
    }
});


var app = new Vue({
    el: '#app'
    , data: data
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
        , editarAsignatura(obj) {
            
            if(obj) {
                //Setear modal
                this.m_asignatura = `${obj.asi_des} ${obj.num_des}`;
                this.m_id_asignatura = obj.asi_id;
                this.m_catedra = obj.cant_horas; 
                this.m_num_id = obj.num_id              
                $('#modal-editar_horas-catedra').modal('show');
                               
            }
        }
    }
    , mounted() {
        this.obtenerAsignaturasCurso();
        this.obtenerTodasAsignaturas();
    }
    , delimiters: ['[[',']]']
})