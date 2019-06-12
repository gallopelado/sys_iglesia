document.addEventListener('DOMContentLoaded', () => {

    // Luego de cargarse el DOM
    let obj = new AdmisionUI();
    obj.iniciarFechas();
    obj.obtenerDatalistPersonas();
    document.getElementById('btnDeshacerTelefono').disabled = true;
    document.getElementById('btnDeshacerPadres').disabled = true;

});

var btLimpiar = document.getElementById('btnLimpiar');
btLimpiar.addEventListener('click', () => {
    
    let tablatelefonos = document.getElementById('tabla_telefonos'),
        rowCountT = tablatelefonos.rows.length,
        tablapadres = document.getElementById('tabla_padres'),
        rowCountP = tablapadres.rows.length;

    for(let i=rowCountP - 1; i > 0 ; i--) {
        tablapadres.deleteRow(i);        
        
    }  
    
    for(let i=rowCountT - 1; i > 0 ; i--) {
        tablatelefonos.deleteRow(i);                
    }  

});

// Evento Click al Boton Agregar Nueva Persona
var btnAgregarPersona = document.getElementById('btnAgregarNuevaPersona');
btnAgregarPersona.addEventListener('click', () => {
    bt = new AdmisionUI();
    bt.mensaje('Mensaje confirmación', 'Desea agregar un nuevo registro de Persona ?');
});

// Evento click al boton Guardar del Formulario 
var btnGuardarPersona = document.getElementById('btnGuardarPersona');
btnGuardarPersona.addEventListener('click', () => {
    bt = new FormularioPersonaUI('a');
    bt.guardar();
});

var campoAgregarTelefono = document.getElementById('txt_telefono');
var lista = new Array();

campoAgregarTelefono.addEventListener('keypress', (e) => {

    // Si activa evento ENTER
    if (e.keyCode == 13) {

        let ad = new AdmisionUI();
        ad.agregarTelefono();
        document.getElementById('txt_telefono').value = "";
        document.getElementById('cbo_tipotel').value = ""; 

    }

});

// Evento click al boton Deshacer del Formulario 
var btDeshacerT = document.getElementById('btnDeshacerTelefono')
btDeshacerT.addEventListener('click', () => {

    // Comprobar elementos en la tabla
    // Obtener datos de la tabla
    let indice, tabla = document.getElementById('tabla_telefonos');

    for (let i = 1; i < tabla.rows.length; i++) {

        console.log(tabla.rows[i].cells[0].parentElement.className);
        let elemento = tabla.rows[i].cells[0].parentElement.className;

        if (elemento === "bg-warning") {
            tabla.rows[i].cells[0].parentElement.className = "";
            document.getElementById('btnDeshacerTelefono').disabled = true;
        }

    }

});


// Evento click al boton Deshacer del Formulario 
var btDeshacerP = document.getElementById('btnDeshacerPadres')
btDeshacerP.addEventListener('click', () => {

    // Comprobar elementos en la tabla
    // Obtener datos de la tabla
    let indice, tabla = document.getElementById('tabla_padres');

    for (let i = 1; i < tabla.rows.length; i++) {

        console.log(tabla.rows[i].cells[0].parentElement.className);
        let elemento = tabla.rows[i].cells[0].parentElement.className;

        if (elemento === "bg-warning") {
            tabla.rows[i].cells[0].parentElement.className = "";
            document.getElementById('btnDeshacerPadres').disabled = true;
        }

    }

});

var campoPadres = document.getElementById('txt_padres');
campoPadres.addEventListener('keypress', (e) => {

    // Si activa evento ENTER
    if (e.keyCode == 13) {

        let ad = new AdmisionUI();
        ad.agregarPadres();
        document.getElementById('txt_padres').value = ""

    }

})

function borrarTelefono() {
    bt = new AdmisionUI();
    bt.borrarTelefono();
}

function borrarPadres() {
    bt = new AdmisionUI();
    bt.borrarPadres();
}

/**
 * Clase principal del movimiento.
 * 
 * Se define toda la funcionalidad para este movimiento.
 * 
 * @author <juanftp100@gmail.com> Juan Jose Gonzalez
 */
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

    agregarTelefono() {

        if (this.controlarTelefonosRepetidos()) {

            // Obtiene datos del formulario
            let tabla = document.getElementById('tabla_telefonos'),

                // Crea la fila
                fila = tabla.insertRow(1),

                telefono = document.getElementById('txt_telefono').value,
                tipotelefono = document.getElementById('cbo_tipotel').value,

                // Crear celdas
                celda1 = fila.insertCell(0),
                celda2 = fila.insertCell(1),
                celda3 = fila.insertCell(2);

            // Agregar celda en la tabla HTML
            celda1.innerHTML = telefono;
            celda2.innerHTML = tipotelefono;
            celda3.innerHTML = "<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='borrarTelefono()'><i class='fa fa-bolt'></i> Borrar</button>";

        } else {
            console.error('Algo paso :-( ');
        }

    }

    borrarTelefono() {

        // Obtener datos de la tabla
        let indice, tabla = document.getElementById('tabla_telefonos'),
            borrar = new Array();

        // Recorrer la tabla
        for (let i = 1; i < tabla.rows.length; i++) {

            // Ligar el evento click al boton dentro de la tabla.
            tabla.rows[i].cells[2].children[0].onclick = function () {

                // Obtener el indice de fila.                
                indice = this.parentElement.parentElement.rowIndex;

                // Borrar fila
                //tabla.deleteRow(indice);

                tabla.rows[i].className = 'bg-warning';

                document.getElementById('btnDeshacerTelefono').disabled = false;

                // Agregar para borrar
                //borrar.push()

            }

        }

    }

    controlarTelefonosRepetidos() {

        // Obtener data del formulario
        let tabla = document.getElementById('tabla_telefonos'),
            telefono = document.getElementById('txt_telefono').value,
            tipotelefono = document.getElementById('cbo_tipotel').value;

        // Validar
        if (telefono.trim() !== "" && tipotelefono !== "") {

            // Recorrer la tabla
            for (let i = 1; i < tabla.rows.length; i++) {

                // Verificar que no se repita el numero de telefono
                if (tabla.rows[i].cells[0].innerHTML === telefono.trim()) {
                    alert('Repetido');
                    return false;
                }

            }

        } else {

            alert("Campo no debe estar vacio");
            return false;

        }

        return true;

    }

    agregarPadres() {

        if (this.controlarPadresRepetidos()) {

            let tabla = document.getElementById('tabla_padres'),
                fila, celda1, celda2,
                padre = document.getElementById('txt_padres').value;

            fila = tabla.insertRow(1);

            celda1 = fila.insertCell(0);
            celda2 = fila.insertCell(1);

            celda1.innerHTML = padre;
            celda2.innerHTML = "<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='borrarPadres()'><i class='fa fa-bolt'></i> Borrar</button>";

        } else {
            console.error('Algo salio mal :-(');
        }

    }

    controlarPadresRepetidos() {

        let tabla = document.getElementById('tabla_padres'),
            padre = document.getElementById('txt_padres').value;

        // Validar
        if (padre.trim() !== "") {

            // Recorrer la tabla
            for (let i = 1; i < tabla.rows.length; i++) {
                console.log(tabla.rows[i].cells[0].innerHTM);
                if (tabla.rows[i].cells[0].innerHTML === padre.trim()) {

                    alert('Repetido');
                    return false;
                }

            }

        } else {

            alert('Campo no debe estar vacio');
            return false;

        }

        return true;

    }

    borrarPadres() {

        // Obtener datos de la tabla
        let indice, tabla = document.getElementById('tabla_padres'),
            borrar = new Array();

        // Recorrer la tabla
        for (let i = 1; i < tabla.rows.length; i++) {

            // Ligar el evento click al boton dentro de la tabla.
            tabla.rows[i].cells[1].children[0].onclick = function () {

                // Obtener el indice de fila.                
                indice = this.parentElement.parentElement.rowIndex;

                // Borrar fila
                //tabla.deleteRow(indice);

                tabla.rows[i].className = 'bg-warning';

                document.getElementById('btnDeshacerPadres').disabled = false;

                // Agregar para borrar
                //borrar.push()

            }

        }

    }

}


/**
 * Clase FormularioPersonaUI
 * 
 * Se define todo lo que tenga que ver con el modal de Formulario Persona.
 * 
 * @author <juanftp100@gmail.com> Juan Jose Gonzalez
 */
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
