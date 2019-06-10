document.addEventListener('DOMContentLoaded', () => {

    // Luego de cargarse el DOM
    let obj = new AdmisionUI();
    obj.iniciarFechas();
    obj.obtenerDatalistPersonas();

});

// Evento Click al Boton Agregar Nueva Persona
var btnAgregarPersona = document.getElementById('btnAgregarNuevaPersona');
btnAgregarPersona.addEventListener('click', () => {
    bt = new AdmisionUI();
    bt.mensaje('Mensaje confirmación', 'Desea agregar un nuevo registro de Persona ?');
});

// Evento click al boton Guardar del Formulario Persona
var btnGuardarPersona = document.getElementById('btnGuardarPersona');
btnGuardarPersona.addEventListener('click', () => {
    bt = new FormularioPersonaUI('a');
    bt.guardar();
});

class AdmisionUI {

    constructor(persona, fechanac, direccion, ciudad, clasisocial, relacionfamiliar, fechamatri,
        email, postal, fechaprimercontacto, estadocivil, sexo, formacontacto, asisteotraigle, visita,
        nuevociudad, conyumiembro, iglesia, fechaultvisita, conyuge, nrohijos) {

        this.persona = document.getElementById('txt_persona');
        this.fechanac = document.getElementById('txt_fechanac');
        this.direccion = document.getElementById('txt_direccion');
        this.ciudad = document.getElementById('cbo_ciudad');
        this.clasisocial = document.getElementById('cbo_clasisocial');
        this.relacionfamiliar = document.getElementById('cbo_rfamiliar');
        this.fechamatri = document.getElementById('txt_fechamatri');
        this.email = document.getElementById('txt_email');
        this.postal = document.getElementById('txt_postal');
        this.fechaprimercontacto = document.getElementById('txt_primercontacto');
        this.estadocivil = document.getElementById('cbo_ecivil');
        this.sexo = sexo;
        this.formacontacto = document.getElementById('cbo_fcontacto');
        this.asisteotraigle = document.getElementById('chk_otraiglesa');
        this.visita = document.getElementById('chk_visita');
        this.nuevociudad = document.getElementById('chk_nuevo');
        this.conyumiembro = document.getElementById('chk_miembroconyuge');
        this.iglesia = document.getElementById('txt_iglesia');
        this.fechaultvisita = document.getElementById('txt_ultimavezcontacto');
        this.conyuge = document.getElementById('txt_conyuge');
        this.nrohijos = document.getElementById('txt_nrohijos');
    }

    hacerDatePicker(id, parametros = null) {

        $("#" + id).datepicker(parametros);

    }

    iniciarFechas() {

        let fechaHoy = new Date().getDate();
        let rangoFecha = "1920:2019";

        this.hacerDatePicker('txt_fechanac', {
            yearRange: rangoFecha,
            changeMonth: true,
            changeYear: true,
            dateFormat: "yy-mm-dd",
            currentText: "now",
            maxDate: new Date(new Date().setDate(fechaHoy))
        });
        this.hacerDatePicker('txt_fechamatri', {
            yearRange: rangoFecha,
            changeMonth: true,
            changeYear: true,
            dateFormat: "yy-mm-dd",
            currentText: "now",
            maxDate: new Date(new Date().setDate(fechaHoy))
        });
        this.hacerDatePicker('txt_primercontacto', {
            yearRange: rangoFecha,
            changeMonth: true,
            changeYear: true,
            dateFormat: "yy-mm-dd",
            currentText: "now",
            maxDate: new Date(new Date().setDate(fechaHoy))
        });
        this.hacerDatePicker('txt_ultimavezcontacto', {
            yearRange: rangoFecha,
            changeMonth: true,
            changeYear: true,
            dateFormat: "yy-mm-dd",
            currentText: "now",
            maxDate: new Date(new Date().setDate(fechaHoy))
        });

        $.datepicker.regional['es'] = {
            closeText: 'Cerrar',
            prevText: '<Ant',
            nextText: 'Sig>',
            currentText: 'Hoy',
            monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
            dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
            dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Juv', 'Vie', 'Sáb'],
            dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sá'],
            weekHeader: 'Sm',
            dateFormat: 'dd/mm/yy',
            firstDay: 1,
            isRTL: false,
            showMonthAfterYear: false,
            yearSuffix: ''
        };
        $.datepicker.setDefaults($.datepicker.regional['es']);

        /***********************************/

    }

    /**
 * Metodo mensaje
 * 
 * Sirve para mostrar mensaje en pantalla, mensajes de confirmacion.
 * 
 * @param {*} titulo 
 * @param {*} contenido 
 * @param {*} url 
 * @param {*} id 
 */
    mensaje(titulo, contenido, url) {
        $.confirm({
            theme: 'supervan',
            title: titulo,
            content: contenido,
            buttons: {
                Si: {
                    text: 'Si',
                    btnClass: 'btn-blue',
                    action: function () {
                        //$('#mediumModal').modal();
                        bt = new AdmisionUI();
                        bt.mostrarFormularioPersona();
                    }
                },
                No: {
                    text: 'No',
                    btnClass: 'btn-red',
                    action: function () {

                    }
                }
            }
        });
    }

    mostrarFormularioPersona() {
        $('#mediumModal').modal();
    }

    async obtenerDatalistPersonas() {
        try {

            const res = await fetch('http://localhost:5000/persona/get_personas');
            const data = await res.text();

            return document.getElementById('lista_personas').innerHTML = data;

        } catch (error) {
            return console.error(error);
        }
    }

    mensajeExito(mensaje, contenido) {
        $.alert({
            title: mensaje,
            content: contenido,
        });
    }

}

class FormularioPersonaUI {

    constructor(op) {
        this.op = op;
        this.cedula = document.getElementById('txtcedula');
        this.tipopersona = document.getElementById('cbo_tipopersona');
        this.nombres = document.getElementById('txtnombres');
        this.apellidos = document.getElementById('txtapellidos');
        this.obs = document.getElementById('txtobs');
    }

    validarForm() {
        if (this.op.trim() != "" && this.cedula.value.trim() != "" && this.nombres.value.trim() != "" && this.apellidos.value.trim() != "") {
            return true;
        }
        return false;
    }

    limpiaForm() {
        this.op = "";
        this.cedula.value = "";
        this.tipopersona.value = "";
        this.nombres.value = "";
        this.apellidos.value = "";
        this.obs.value = "";
    }

    recuperaDatosForm() {

        let formulario = new FormData();
        formulario.append('op', this.op);
        formulario.append('txtcedula', this.cedula.value.trim());
        formulario.append('tipopersona', this.tipopersona.value);
        formulario.append('txtnombres', this.nombres.value.trim());
        formulario.append('txtapellidos', this.apellidos.value.trim());
        formulario.append('txtobs', this.obs.value.trim());

        return formulario;
    }

    async guardar() {
        if (this.validarForm()) {

            //Proceder            
            try {

                const res = await fetch('http://localhost:5000/persona/guardar_persona_ajax', {
                    method: 'POST',
                    body: this.recuperaDatosForm()
                });
                const data = await res.json();
                if (data.estado == true) {

                    $('#mediumModal').modal('toggle');
                    this.limpiaForm();
                    
                    let ad = new AdmisionUI();
                    ad.obtenerDatalistPersonas();
                    ad.mensajeExito('Agregar Persona Exitosa', 'Agregaste una persona!');

                    return data.estado;
                }

                return data.estado;

            } catch (error) {
                console.error('Algo malo ha pasado.');
                return console.error(error);
            }

        }
        return console.log('Algo salio mal.')
    }
}
