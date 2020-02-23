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
        , estadoChecksgroup1:true
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
    }
    , delimiters: ['[[',']]']
});
$('select').select2({});