document.addEventListener('DOMContentLoaded', () => {

    // Luego de cargarse el DOM
    let obj = new AdmisionUI();
    obj.iniciarFechas();
    obj.obtenerDatalistPersonas();
    document.getElementById('btnDeshacerTelefono').disabled = true;
    document.getElementById('btnDeshacerPadres').disabled = true;
    obj.recuperaId();
});

// Definiciones de los eventos de botones

var btLimpiar = document.getElementById('btnLimpiar');
btLimpiar.addEventListener('click', () => {

    let tablatelefonos = document.getElementById('tabla_telefonos'),
        rowCountT = tablatelefonos.rows.length,
        tablapadres = document.getElementById('tabla_padres'),
        rowCountP = tablapadres.rows.length,
        ad = new AdmisionUI()
    ad.limpiaForm();

    for (let i = rowCountP - 1; i > 0; i--) {
        tablapadres.deleteRow(i);

    }

    for (let i = rowCountT - 1; i > 0; i--) {
        tablatelefonos.deleteRow(i);
    }

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

        //console.log(tabla.rows[i].cells[0].parentElement.className);
        let elemento = tabla.rows[i].cells[0].parentElement.className;

        if (elemento === "bg-warning text-white") {
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

        //console.log(tabla.rows[i].cells[0].parentElement.className);
        let elemento = tabla.rows[i].cells[0].parentElement.className;

        if (elemento === "bg-warning text-white") {
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

    }

});

var btnGuardarFormAdmision = document.getElementById('btnGuardarFormAdmision');
btnGuardarFormAdmision.addEventListener('click', () => {

    ad = new AdmisionUI();
    ad.guardar();

});

// Funciones
function mensajeAlert(id, titulo='Titulo', mensaje='Mensaje', clasemensaje='alert-success') {
    
    let cadena = `
    <div class="sufee-alert alert with-close ${clasemensaje} alert-dismissible fade show">
		<span class="badge badge-pill badge-success">${titulo}</span>
			${clasemensaje}.
		<button type="button" class="close" data-dismiss="alert" aria-label="Close">
		    <span aria-hidden="true">×</span>
		</button>
	</div>
    `;
    //Aplicar a un div
    caja = document.getElementById(`${id}`);
    caja.innerHTML = cadena;
    setTimeout(() => {
        caja.innerHTML = '';
    }, 3000 )
    
}

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

    constructor() {
        this.idadmision = document.getElementById('idadmision');
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
        this.sexoM = document.getElementById('chk_masculino');
        this.sexoF = document.getElementById('chk_femenino');
        this.formacontacto = document.getElementById('cbo_fcontacto');
        this.asisteotraigle = document.getElementById('chk_otraiglesa');
        this.visita = document.getElementById('chk_visita');
        this.nuevociudad = document.getElementById('chk_nuevo');
        this.iglesia = document.getElementById('txt_iglesia');
        this.fechaultvisita = document.getElementById('txt_ultimavezcontacto');
        this.conyuge = document.getElementById('txt_conyuge');
        this.nrohijos = document.getElementById('txt_nrohijos');
        this.familia = document.getElementById('cbo_familia');
        this.tablatelefonos = document.getElementById('tabla_telefonos');
        this.tablapadres = document.getElementById('tabla_padres');
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
                fila = tabla.insertRow(),

                telefono = document.getElementById('txt_telefono').value,
                tipotelefono = document.getElementById('cbo_tipotel').value,

                // Crear celdas
                celda1 = fila.insertCell(0),
                celda2 = fila.insertCell(1),
                celda3 = fila.insertCell(2);

            //fila.className = 'btn-outline-success';                
            fila.style.backgroundColor = '#C0DF81';

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
                tabla.rows[i].className = 'bg-warning text-white';

                document.getElementById('btnDeshacerTelefono').disabled = false;

                // Borra la fila segun el estilo de color #C0DF81, pasado a RGB.
                if (tabla.rows[i].style.backgroundColor === 'rgb(192, 223, 129)') {
                    tabla.deleteRow(indice);
                    return;
                }

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

    async agregarPadres() {

        if (this.controlarPadresRepetidos()) {


            if (await this.controlarExistenciaPadres()) {

                let tabla = document.getElementById('tabla_padres'),
                    fila, celda1, celda2, celda3,
                    padre = document.getElementById('txt_padres').value;

                fila = tabla.insertRow();

                fila.style.backgroundColor = '#C0DF81';
                celda1 = fila.insertCell(0);
                celda2 = fila.insertCell(1);
                celda3 = fila.insertCell(2);

                celda1.innerHTML = "#";
                celda2.innerHTML = padre;
                celda3.innerHTML = "<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='borrarPadres()'><i class='fa fa-bolt'></i> Borrar</button>";

                document.getElementById('txt_padres').value = ""

            } else {
                alert('Esta persona no existe, favor registrarla');
            }

        }

    }

    controlarPadresRepetidos() {

        let tabla = document.getElementById('tabla_padres'),
            padre = document.getElementById('txt_padres').value;

        // Validar
        if (padre.trim() !== "") {

            // Recorrer la tabla
            for (let i = 1; i < tabla.rows.length; i++) {

                //console.log(tabla.rows[i].cells[0].innerHTML);

                if (tabla.rows[i].cells[1].innerHTML === padre.trim()) {

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

    async controlarExistenciaPadres() {
        try {

            // Obtener datos del campo
            let campo = document.getElementById('txt_padres').value.trim(),

                // Si queres usar el objeto formData(), no hace falta especificar headers en fetch
                //form = new FormData(),
                //form.append('palabra', campo);            

                objeto = { palabra: campo };

            const res = await fetch('http://localhost:5000/formulario_admision/buscar_padre_ajax', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(objeto)
            });

            const data = await res.json();

            return data.existe;

        } catch (error) {
            console.error(error);
            return false;
        }
    }

    borrarPadres() {

        // Obtener datos de la tabla
        let indice, tabla = document.getElementById('tabla_padres'),
            borrar = new Array();

        // Recorrer la tabla
        for (let i = 1; i < tabla.rows.length; i++) {

            // Ligar el evento click al boton dentro de la tabla.
            tabla.rows[i].cells[2].children[0].onclick = function () {

                // Obtener el indice de fila.                
                indice = this.parentElement.parentElement.rowIndex;

                // Borrar fila
                //tabla.deleteRow(indice);

                tabla.rows[i].className = 'bg-warning text-white';

                document.getElementById('btnDeshacerPadres').disabled = false;

                // Borra fila segun el estilo de color #C0DF81, pasado a RGB.
                if (tabla.rows[i].style.backgroundColor === 'rgb(192, 223, 129)') {
                    tabla.deleteRow(indice);
                    return;
                }

            }

        }

    }

    // Metodos para preparar el guardado

    limpiaForm() {

        const arrayjIds = [

            "txt_persona",
            "txt_fechanac",
            "txt_direccion",
            "cbo_ciudad",
            "cbo_clasisocial",
            "cbo_rfamiliar",
            "txt_fechamatri",
            "txt_email",
            "txt_postal",
            "txt_primercontacto",
            "cbo_ecivil",
            "cbo_fcontacto",
            "txt_iglesia",
            "txt_ultimavezcontacto",
            "txt_conyuge",
            "txt_nrohijos",
            "cbo_familia"

        ];

        for (let i = 0; i < arrayjIds.length; i++) {

            document.getElementById(`${arrayjIds[i]}`).value = "";

        }

    }

    validarForm() {

        const arrayjIds = [

            "txt_persona",
            "txt_fechanac",
            "txt_direccion",
            "cbo_ciudad",
            "cbo_clasisocial",
            "cbo_rfamiliar",
            "cbo_ecivil",
            "cbo_fcontacto",
            "cbo_familia"

        ];


        for (let i = 0; i < arrayjIds.length; i++) {

            if (document.getElementById(`${arrayjIds[i]}`).value.trim() === "" || document.getElementById(`${arrayjIds[i]}`).value === null) {

                document.getElementById(`${arrayjIds[i]}`).focus();
                return false;

            }

        }

        return true;

    }

    /**
     * Metodo obtenerDatosFormulario.
     * 
     * Recuperar datos del formulario.
     * 
     */
    obtenerDatosFormulario() {

        if (this.validarForm()) {

            let tablatelefonos, tablapadres, dataTotal,
                formulario = {
                    idadmision: this.idadmision.value.trim(),
                    idpersona: this.persona.value.trim(),
                    fechanac: this.fechanac.value.trim(),
                    direccion: this.direccion.value.trim(),
                    idciudad: this.ciudad.value.trim(),
                    idsocial: this.clasisocial.value.trim(),
                    idfamilar: this.relacionfamiliar.value.trim(),
                    fechamatri: this.fechamatri.value.trim(),
                    email: this.email.value.trim(),
                    postal: this.postal.value.trim(),
                    fechaprimercontacto: this.fechaprimercontacto.value.trim(),
                    ecivil: this.estadocivil.value.trim(),
                    sexo: this.saberSexo(),
                    formacontacto: this.formacontacto.value.trim(),
                    asisteotraigle: this.asisteotraigle.checked,
                    requierevisita: this.visita.checked,
                    nuevociudad: this.nuevociudad.checked,
                    //conyumiembro: this.conyumiembro.checked,
                    iglesia: this.iglesia.value.trim(),
                    fechaultvisita: this.fechaultvisita.value.trim(),
                    idconyuge: this.conyuge.value.trim(),
                    nrohijos: this.nrohijos.value.trim(),
                    familia: this.familia.value.trim()

                };

            // Recolectar telefonos de la tabla
            tablatelefonos = this.tablatelefonos;

            let borrarTel = [], agregarTel = [], nuevosPadres = [], borrarPadres = [], cont = 0, contE = 0;

            for (let i = 1; i < tablatelefonos.rows.length; i++) {

                // Obtener numero de columna.
                let indiceTel = tablatelefonos.rows[i].rowIndex;

                // Separamos los registros nuevos que tenga ese estilo.
                if (tablatelefonos.rows[i].style.backgroundColor === 'rgb(192, 223, 129)') {

                    // Se analiza el primer indice que no es cero, para no dejar un empty slot.                                            
                    agregarTel[cont] = {
                        "id": cont,
                        "tipo": tablatelefonos.rows[i].cells[1].innerHTML,
                        "numero": tablatelefonos.rows[i].cells[0].innerHTML
                    }
                    cont = cont + 1;
                    // Separamos los registros para borrarse que tenga esa clase.
                } else if (tablatelefonos.rows[i].className === 'bg-warning text-white') {

                    borrarTel[contE] = {
                        "id": i,
                        "tipo": tablatelefonos.rows[i].cells[1].innerHTML,
                        "numero": tablatelefonos.rows[i].cells[0].innerHTML
                    }
                    contE = contE + 1;
                }

            }

            // Recolectar padres de la tabla
            tablapadres = this.tablapadres;

            for (let i = 1; i < tablapadres.rows.length; i++) {

                // Agregar al array los nuevos padres.
                if (tablapadres.rows[i].style.backgroundColor === 'rgb(192, 223, 129)') {

                    //Objeto
                    let objeto = {
                        "idpadre": tablapadres.rows[i].cells[0].innerHTML,
                        "persona": tablapadres.rows[i].cells[1].innerHTML
                    }

                    nuevosPadres.push(
                        objeto
                    );
                    // Agrega al array los padres a eliminarse.
                } else if (tablapadres.rows[i].className === 'bg-warning text-white') {

                    //Objeto
                    let objeto = {
                        "idpadre": tablapadres.rows[i].cells[0].innerHTML,
                        "persona": tablapadres.rows[i].cells[1].innerHTML
                    }

                    borrarPadres.push(
                        objeto
                    );
                }

            }

            dataTotal = {
                formulario: formulario,
                borrarTel: borrarTel,
                agregarTel: agregarTel,
                nuevosPadres: nuevosPadres,
                borrarPadres: borrarPadres
            }

            return dataTotal;

        } else {
            console.error('Error de validacion');
            return false;
        }

    }

    saberSexo() {
        if (this.sexoM.checked) {
            return "MASCULINO";
        } else {
            return "FEMENINO";
        }
    }

    async guardar() {

        // Recuperar datos del formulario.
        let formulario = this.obtenerDatosFormulario();

        console.log(formulario);

        if (formulario !== false) {

            try {

                const res = await fetch('http://localhost:5000/formulario_admision/modificar', {

                    method: 'POST',
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formulario)

                });
                const data = await res.json();

                console.log(data);
                if (data.guardado === true) {
                    this.limpiaForm();
                    document.getElementById('btnLimpiar').click();
                    window.location.href = 'http://localhost:5000/formulario_admision/';
                }

            } catch (error) {

                return console.log(error);

            }

        }

    }

    recuperaId() {

        // Obtener el ultimo numerito de la URL que es el id, mediante un array.
        let arrayUrl = window.location.href.split('/'),
            idadmision = arrayUrl[5];

        this.procesarDatos(idadmision);
        this.obtenerTelefonos(idadmision);
        this.obtenerPadres(idadmision);

    }

    async obtenerDatosFormularioId(id) {

        let datos = {
            idadmision: id
        }

        try {

            const res = await fetch('http://localhost:5000/formulario_admision/obtener_formulario_id', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            return data;

        } catch (error) {
            console.error(error);
            return false;
        }


    }

    async procesarDatos(id) {

        // Obtenemos datos del servidor.
        let data = await this.obtenerDatosFormularioId(id);

        // Setear formulario
        this.idadmision.value = data[0];
        this.persona.value = data[21];
        this.fechanac.value = data[1];
        this.direccion.value = data[2];
        this.ciudad.value = data[3];
        this.clasisocial.value = data[4];
        this.relacionfamiliar.value = data[7];
        this.fechamatri.value = data[9];
        this.email.value = data[10];
        this.postal.value = data[11];
        this.fechaprimercontacto.value = data[15];
        this.estadocivil.value = data[5];
        this.sexoM.checked = data[6] === 'MASCULINO' ? true : false;
        this.sexoF.checked = data[6] === 'FEMENINO' ? true : false;
        this.formacontacto.value = data[12];
        this.asisteotraigle.checked = data[13];
        this.visita.checked = data[16];
        this.nuevociudad.checked = data[17];
        this.iglesia.value = data[14];
        this.fechaultvisita.value = data[18];
        this.conyuge.value = data[19];
        this.nrohijos.value = data[20];
        this.familia.value = data[8];

        // Procesar datos para telefonos.

    }

    /**
     * Metodo obtenerTelefonos.
     * 
     * Se obtiene la lista de telefonos registrados por formulario.(ASINCRONO)
     * Agrega los registros encontrados en filas HTML.
     * 
     * @param {*} id 
     */
    async obtenerTelefonos(id) {

        let data = {
            idadmision: id
        },
            tabla = document.getElementById('tb_telefonos'),
            cadena = "";

        try {

            const res = await fetch('http://localhost:5000/formulario_admision/obtener_telefonos_id', {

                method: 'POST',
                headers: {

                    'Accept': 'application/json',
                    'Content-Type': 'application/json'

                },
                body: JSON.stringify(data)

            });

            const datos = await res.json();

            //Procesar telefonos.
            for (let i = 0; i < datos.length; i++) {

                cadena += `                
                    <tr>
                        <td>${datos[i][3]}</td>
                        <td>${datos[i][1]}</td>
                        <td>
                            <button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='borrarTelefono()'><i class='fa fa-bolt'></i> Borrar</button>
                        </td>
                    </tr>                
                `;

            }
            // Cargamos en el tbody del telefonos            
            tabla.innerHTML = cadena;

        } catch (error) {
            console.log(error);
            return false;
        }

    }

    /**
     * Metodo obtenerPadres.
     * 
     * Se obtiene la lista de padres espirituales registrados por formulario.(ASINCRONO)
     * Agrega los registros encontrados en filas HTML.
     * 
     * @param {*} id 
     */
    async obtenerPadres(id) {

        let data = {
            idadmision: id
        },
            tabla = document.getElementById('tb_padres'),
            cadena = "";

        try {

            const res = await fetch('http://localhost:5000/formulario_admision/obtener_padres_id', {

                method: 'POST',
                headers: {

                    'Accept': 'application/json',
                    'Content-Type': 'application/json'

                },
                body: JSON.stringify(data)

            });

            const datos = await res.json();

            //Procesar padres.
            for (let i = 0; i < datos.length; i++) {

                cadena += `
                
                    <tr>
                        <td>${datos[i][0]}</td>
                        <td>${datos[i][1]}</td>                        
                        <td>
                            <button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='borrarPadres()'><i class='fa fa-bolt'></i> Borrar</button>
                        </td>
                    </tr>
                
                `

            }
            // Cargamos en el tbody del telefonos
            tabla.innerHTML = cadena;

        } catch (error) {
            console.log(error);
            return false;
        }

    }

}
