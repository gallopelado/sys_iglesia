Vue.directive('select', {
    twoWay: true,
    bind: function (el, binding, vnode) {
      $(el).select2().on("select2:select", (e) => {
        // v-model looks for
        //  - an event named "change"
        //  - a value with property path "$event.target.value"
        el.dispatchEvent(new Event('change', { target: e.target }));
      });
    },
});

var app = new Vue({
    el:'#app'
    , data:{
        miembro:''
        , edad:''
        , ecivil:''
        , conyuge:''
        , edadconyuge:''
        , tiempocasado:''
        , religion:''
        , descrimatri:''
        , descrihijos:''
        , asisteregular:false
        , servicioncentral:false
        , grupo: ''
        , serviciosemanal:false
        , asistegrupo:''
        , consultagrupo:false
        , descrirecibio:''
        , descriasesoria:''
        , consejero:''
        , descrimatri:''
        , datosMiembro:{}
        , datosEditar:{}
        , estadoChecksgroup1:true
        , bloqueado: false
    }
    , methods: {
        cargaDatosMiembro: async function (){
            try {                
                const res = await axios.get(`/actividades/consejeria/get_miembros/${this.miembro}`);
                this.datosMiembro = await res.data[0];
                const {conyuge, ecivil, edad, edadconyuge, idconyuge, idmiembro, miembro, tiempocasado} = this.datosMiembro;
                this.edad = edad;
                this.ecivil = ecivil;
                this.conyuge = conyuge;
                this.edadconyuge = edadconyuge;
                this.tiempocasado = tiempocasado;
            } catch (error) {
                console.error(error);
            }
        }
        , habilitaChecksGroup1: function() {  
            //this.estadoChecksgroup1 = false;         
            if(this.asisteregular == true) {                
                this.estadoChecksgroup1 = false;
                return;
            } 
            this.estadoChecksgroup1 = true;
            this.servicioncentral = false;
            this.grupo = false;
            this.serviciosemanal = false;
        }
        , validaFormulario: function() {            
            if(!this.miembro) {
                alert('Elija una opcion');
               $('#miembro').focus(); 
                return false;                           
            }
            if(!this.religion) {
                alert('Elija una opcion');
                $('#religion').focus();                
                return false;                
            }
            if(this.asisteregular && (!this.servicioncentral && !this.grupo && !this.serviciosemanal)) {
                alert('Si asiste regularmente, debe selecciona una de las opciones');
                $('#asiste_regular').focus();                
                return false;                
            }
            if(this.consultagrupo && !this.asistegrupo) {
                alert('Si consulto a un grupo, debe elegir uno');
                $('#grupo_asiste').focus();
                return false;
            }
            if(!this.descrirecibio) {
                alert('Completar campo');
                $('#descri_recibio').focus();
                return false;
            }
            if(!this.descriasesoria) {
                alert('Completar campo');
                $('#descri_asesoria').focus();
                return false;
            }
            if(!this.consejero) {
                alert('Elegir consejero');
                $('#consejero').focus();
                return false;
            }
           
            $('#form').submit();            
        }
        , cargarFormulario: async function () {
            if(localStorage.getItem('idsolicitud')) {
                this.estadoChecksgroup1 = false;
                try {                
                    const res = await axios.get(`/actividades/consejeria/get_solicitud_id/${localStorage.getItem('idsolicitud')}`);
                    this.datosEditar = await res.data;
                    const d = this.datosEditar;
                    this.miembro = d.idsolicitante;
                    $('#miembro').val(d.idsolicitante);
                    $('#miembro').trigger('change');
                    this.edad = d.edad;
                    this.ecivil = d.ecivil;
                    this.conyuge = d.conyuge;
                    this.edadconyuge = d.edadconyuge;
                    this.tiempocasado = d.tiempocasado;
                    this.religion = d.idreligion;
                    $('#religion').val(d.idreligion);
                    $('#religion').trigger('change');
                    this.servicioncentral = d.servcentral;
                    this.grupo = d.gruposcrecimiento;
                    this.serviciosemanal = d.servsemana;
                    this.descrimatri = d.descrmatriant;
                    this.descrihijos = d.descr_hijos;
                    this.asistegrupo = d.idgrupo;
                    $('#grupo_asiste').val(d.idgrupo);
                    $('#grupo_asiste').trigger('change');
                    this.consultagrupo = d.consultogrupo;
                    this.descrirecibio = d.convertido;
                    this.descriasesoria = d.asesoria;
                    this.consejero = d.idconsejero;
                    $('#consejero').val(d.idconsejero);
                    $('#consejero').trigger('change');
                } catch (error) {
                    console.error(error);
                }
            }
        }           
    }
    , beforeMount() {
        this.cargarFormulario();
        this.bloqueado = bloqueado;   
    }
    , delimiters: ['[[',']]']
});
$('select').select2({});