document.addEventListener('DOMContentLoaded', () => {
    let adi = new FormAdicionalUI();
    adi.cargarComboProfesion();
    adi.setearFormulario();
});

// Eventos para botones.
var btnAgregarTabla = document.getElementById('btnAgregarDatos');
btnAgregarTabla.addEventListener('click', () => {

    let adi = new FormAdicionalUI();
    adi.agregarProfesiones();

});

var btnAgregarProfesion = document.getElementById('btnAgregarProfesion');
btnAgregarProfesion.addEventListener('click', () => {

    let modal = new ModalProfesion();

    // Generar una instancia de jqueryconfirm.
    let c = mensajeConfirmacion('Mensaje de confirmación', 'Desea agregar una nueva profesión/oficio?');
    c.buttons.Si.action = () => modal.mostrar();
    c.open();

});

var btnGuardarFormAdicional = document.getElementById('btnGuardarFormAdicional');
btnGuardarFormAdicional.addEventListener('click', () => {

    let adi = new FormAdicionalUI();
    adi.guardarFormulario();
    //adi.recuperaDatosFormulario();

});

var btnLimpiar = document.getElementById('btnLimpiar');
btnLimpiar.addEventListener('click', () => {

    let adi = new FormAdicionalUI();
    adi.limpiarFormulario();

});

// Evento Formulario Foto
const frmFoto = document.getElementById('frmFoto');
frmFoto.addEventListener('submit', e => {

    // Se previene el comportamiento nativo del formulario.
    e.preventDefault();

    let adi = new FormAdicionalUI();
    adi.guardarFoto();

});

// Evento change para campo input file.
const btnBrowse = document.getElementById('txt_foto');
btnBrowse.addEventListener('change', () => {

    let elemImage = document.getElementById('img_foto');

    let reader = new FileReader();

    reader.onload = e => {
        // Convierte a Base64, y carga en el atributo de la imagen.
        elemImage.src = e.target.result;
    }

    // Con este metodo leemos ese de Base64 a url.
    reader.readAsDataURL(btnBrowse.files[0])

});

// Funciones
function eliminarFila() {
    let adi = new FormAdicionalUI();
    adi.eliminarFila();
}

class FormAdicionalUI {

    constructor() {

        this.idpersona = document.getElementById('idpersona');
        this.persona = document.getElementById('txt_persona');
        this.idnacionalidad = document.getElementById('cbo_nacionalidad');
        this.lugarnacimiento = document.getElementById('txt_lugarnac');
        this.alergia = document.getElementById('txt_alergia');
        this.tiposangre = document.getElementById('cbo_tiposangre');
        this.capacidades = document.getElementById('txt_capacidades');
        this.foto = document.getElementById('txt_foto');
        this.idprofesion = document.getElementById('cbo_profesion');
        this.puesto = document.getElementById('txt_puesto');
        this.lugartrabajo = document.getElementById('txt_lugartrabajo');

    }

    agregarProfesiones() {

        let fila, celda0, celda1, celda2, celda3, celda4, tabla = document.getElementById('tabla_profesiones'),
            boton = `<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='eliminarFila()'><i class='fa fa-minus-square'></i> Eliminar</button>`;



        // Se buscar cual es la opcion que ha sido seleccionada.
        // Siendo asi, se recuper id, nombre de profesion para la tabla.
        for (let i = 0; i < this.idprofesion.length; i++) {

            if (this.idprofesion.value !== "" && this.puesto.value.trim() !== "" && this.lugartrabajo.value.trim() !== "") {

                if (this.idprofesion.children[i].selected === true) {
                    //console.log(`Seleccionado id:${this.idprofesion.children[i].id} es ${this.idprofesion.children[i].value}`);                   

                    if (this.controlarRepetidos() !== true) {

                        // Crear filas.
                        fila = tabla.insertRow();
                        // Se define un color de fondo para la fila.
                        fila.style.backgroundColor = '#C0DF81';

                        // Crear celdas.
                        celda0 = fila.insertCell(0);
                        celda1 = fila.insertCell(1);
                        celda2 = fila.insertCell(2);
                        celda3 = fila.insertCell(3);
                        celda4 = fila.insertCell(4);

                        // Asignar variables
                        let idprofesion = "", descriprofesion = "", puesto = "", lugartrabajo = "";
                        idprofesion = this.idprofesion.children[i].id;
                        descriprofesion = this.idprofesion.children[i].value;
                        puesto = this.puesto.value.trim();
                        puesto = puesto.toUpperCase();
                        lugartrabajo = this.lugartrabajo.value.trim();
                        lugartrabajo = lugartrabajo.toUpperCase();

                        // Se agrega contenido a la tabla.
                        celda0.innerHTML = idprofesion;
                        celda1.innerHTML = descriprofesion;
                        celda2.innerHTML = puesto;
                        celda3.innerHTML = lugartrabajo;
                        celda4.innerHTML = boton;

                        // limpiar campos
                        this.idprofesion.value = "";
                        this.puesto.value = "";
                        this.lugartrabajo.value = "";
                        camposNoValidos(false);
                        break;

                    } else {
                        alert('Hay campos repetidos.');
                        camposNoValidos(true);
                        break;
                    }

                }
            } else {
                alert('No se permiten campos vacíos.');
                camposNoValidos(true);
                break;
            }

        }

    }

    controlarRepetidos() {

        // Capturar datos
        let tabla = document.getElementById('tabla_profesiones'), descriprofesion = "", puesto = "", lugartrabajo = "";
        descriprofesion = this.idprofesion.value;
        puesto = this.puesto.value.trim();
        puesto = puesto.toUpperCase();
        lugartrabajo = this.lugartrabajo.value.trim();
        lugartrabajo = lugartrabajo.toUpperCase();

        for (let i = 1; i < tabla.rows.length; i++) {

            if (tabla.rows[i].cells[1].innerHTML === descriprofesion && tabla.rows[i].cells[2].innerHTML === puesto && tabla.rows[i].cells[3].innerHTML === lugartrabajo) {
                return true;
            }

        }

        return false;

    }

    eliminarFila() {

        let fila, tabla = document.getElementById('tabla_profesiones');

        for (let i = 1; i < tabla.rows.length; i++) {

            //console.log(tabla.rows[i].cells[4].children[0].parentElement.parentElement.rowIndex);

            tabla.rows[i].cells[4].children[0].onclick = function () {

                // El this indica lo que hay en tabla.rows[i].cells[4].children[0]
                //console.log(this.parentElement.parentElement);
                // Se obtiene el indice del tr, el indice fila.
                fila = this.parentElement.parentElement.rowIndex;

                // Se borra la fila.
                // Si es nuevo, puede borrarse desde la vista.
                if (this.parentElement.parentElement.style.backgroundColor === 'rgb(192, 223, 129)') {
                    if (confirm('Desea eliminarlo ?')) {

                        tabla.deleteRow(fila);

                    }

                } else if (this.parentElement.parentElement.style.backgroundColor === 'rgb(241, 243, 232)') {

                    if (confirm('Este registro existe en la base de datos, desea eliminarlo ?')) {

                        // recuperar ciertos datos de la tabla.
                        // idpersona, idprofesion, puesto_laboral, lugar_trabajo                                                
                        // Proceso para eliminar
                        let adi = new FormAdicionalUI();
                        let data = {
                            id: adi.idpersona.value,
                            idprofesion: tabla.rows[i].cells[0].innerHTML,
                            puesto: tabla.rows[i].cells[2].innerHTML,
                            lugar: tabla.rows[i].cells[3].innerHTML
                        }
                        adi.eliminarHistorial(data);

                    }


                }

            }

        }

    }

    async eliminarHistorial(obj) {

        console.log(obj);
        // Asignamos a una constante para que deje de joder. :-D
        const data = obj;

        try {

            const res = await fetch('http://localhost:5000/formulario_adicional/eliminar_historial', {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });
            const d = await res.json();

            //console.log(d);
            if (d.eliminado === true)
                this.cargarTabla();

        } catch (error) {

            console.error(error);

        }

    }
    async comboProfesion() {

        try {

            const res = await fetch('http://localhost:5000/profesion/listar_profesiones');
            const data = await res.json();

            return data;

        } catch (error) {
            console.error(error);
            return false;
        }
    }

    async cargarComboProfesion() {

        let select = document.getElementById('cbo_profesion'),
            option, profesiones = await this.comboProfesion();

        for (let i = 0; i < profesiones.length; i++) {

            option = document.createElement('option');
            option.text = profesiones[i][1];
            option.value = profesiones[i][1]
            option.id = profesiones[i][0];
            select.add(option);

        }

    }

    refrescarComboProfesion() {

        // Proceso para refrescar el combo de profesiones.
        //# Se obtiene el objeto cbo_profesion.
        let select = document.getElementById('cbo_profesion');

        //# Mientras tenga el primer hijo, eliminar.
        while (select.firstChild) {
            select.removeChild(select.firstChild);
        }

        //# Se crea el primer hijo con el texto Elegir.
        let opcion = document.createElement('option');
        opcion.text = 'Elegir..';
        opcion.selected = true;
        select.add(opcion);

        //# Se instancia un objeto del formulario para ejecutar el metodo que llena el combo.
        this.cargarComboProfesion();

    }

    async obtenerDatosFormId() {

        let datos = {
            idadi: obtenerIdUrl()
        }

        try {

            const res = await fetch('http://localhost:5000/formulario_adicional/obtener_frmdatos_id', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            if (data) {
                return data;
            } else {
                console.error(data);
            }

        } catch (error) {
            console.error(error);
        }

    }

    async obtenerHistorialProfesiones() {

        let datos = {
            idadi: obtenerIdUrl()
        }

        try {

            const res = await fetch('http://localhost:5000/formulario_adicional/obtener_historial_profesiones', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            if (data) {
                return data;
            } else {
                console.error(data);
            }

        } catch (error) {
            console.error(error);
        }

    }

    async setearFormulario() {

        const data = await this.obtenerDatosFormId();

        this.idpersona.value = data[0];
        this.persona.value = data[1] !== null ? data[1] : "";
        this.idnacionalidad.value = data[2] !== null ? data[2] : "";
        this.lugarnacimiento.value = data[3] !== null ? data[3] : "";
        this.tiposangre.value = data[4] !== null ? data[4] : "";
        this.alergia.innerHTML = data[5] !== null ? data[5] : "";
        this.capacidades.innerHTML = data[6] !== null ? data[6] : "";

        this.cargarTabla();

    }

    async cargarTabla() {

        const dataHistorial = await this.obtenerHistorialProfesiones();

        //console.table(dataHistorial[0]);

        let tabla = document.getElementById('tbody_profesiones'), cadena = "", botonEliminar = "", aviso = "";
        botonEliminar = `<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='eliminarFila()'><i class='fa fa-minus-square'></i> Eliminar</button>`;
        aviso = "No hay registros";

        // Limpiar el tbody de la tabla.
        tabla.innerHTML = "";

        // Verificar si no esta vacio.
        if (dataHistorial[0]) {
            // Recorrer el array.
            dataHistorial[0].forEach(valor => {

                cadena += `
                    <tr style="background-color: #F1F3E8">
                        <td>${valor.idprofesion}</td>
                        <td>${valor.profesion}</td>
                        <td>${valor.puesto_laboral}</td>
                        <td>${valor.lugar_trabajo}</td>
                        <td>${botonEliminar}</td>
                    </tr>
                `
            });
            tabla.innerHTML = cadena;

        } else {
            tabla.innerHTML = aviso;
        }

    }

    guardarFoto() {

        // Obtener id del formulario.
        const idadi = this.idpersona.value,
            extensiones_permitidas = ['JPEG'],
            tama_permitido = 1024;



        // Obtener campo File.
        let f = document.getElementById('txt_foto'),
            foto = f.files[0];

        if (typeof (foto) !== 'undefined') {

            // Validar por extension.
            let extensionFile = foto.type.split('/')[1];

            // Se convierte a mayuscula.
            extensionFile = extensionFile.toUpperCase();

            // Tamaño de la imagen con redondeo.
            const tamaImagen = Math.round(foto.size / 1024);
            let nopermitida = true;

            // Validar tamaño de la foto.
            if (tamaImagen <= tama_permitido) {

                // Recorrer en busca de extensiones correctas.
                for (let i = 0; i < extensiones_permitidas.length; i++) {

                    // Verifica extension.
                    if (extensionFile === extensiones_permitidas[i]) {

                        // Se convierte a minúsculas.
                        extensionFile = extensionFile.toLowerCase();

                        // Concatenar el id + extension.
                        let newNombre = `${idadi}.${extensionFile}`;

                        // Sobreescribir la propiedad name con el id del formulario.
                        Object.defineProperty(foto, 'name', {
                            writable: true,
                            value: newNombre,
                            enumerable: true,
                            configurable: true
                        });


                        let formFoto = new FormData();
                        formFoto.append('idadi', idadi);
                        formFoto.append('foto', foto, newNombre);

                        nopermitida = false;

                        // Enviar imagen
                        this.enviarImagen(formFoto);

                        break;

                    }

                }

                if (nopermitida === true)
                    alert('Solo se permiten imagenes JPEG');

            } else {

                alert('Tamaño no permitido hasta 1024 KB');

            }

        }

    }

    async enviarImagen(objeto) {

        try {

            const res = await fetch('http://localhost:5000/formulario_adicional/image_upload', {
                method: 'POST',
                body: objeto
            });
            const data = await res.json();

            //console.log(data);
            if (data.guardado === true) {

                // Se crea la instancia del mensaje de confirmacion.
                let v = mensajeNormal('Éxito', 'Se agregó la foto');
                v.open();

            }                

        } catch (error) {
            console.error(error);
        }

    }

    recuperaDatosFormulario() {

        // Se recuperan los datos del formulario.
        const datosForm = {
            'idpersona': this.idpersona.value,
            'idnacionalidad': this.idnacionalidad.value,
            'lugarnacimiento': this.lugarnacimiento.value,
            'alergias': this.alergia.value.trim(),
            'tiposangre': this.tiposangre.value,
            'capacidad_diferente': this.capacidades.value.trim()
        };

        // Se recupera datos de la tabla segun color.
        let tabla = document.getElementById('tabla_profesiones');
        let lista_nuevas_profesiones = [];

        for (let i = 1; i < tabla.rows.length; i++) {

            //console.log(tabla.rows[i]);
            // Verificar si el estilo es el de agregar.
            if (tabla.rows[i].style.backgroundColor === 'rgb(192, 223, 129)') {

                // Agregar al array de nuevos registros.
                lista_nuevas_profesiones.push(
                    {
                        idprofesion: tabla.rows[i].cells[0].innerHTML,
                        puesto: tabla.rows[i].cells[2].innerHTML,
                        lugartrabajo: tabla.rows[i].cells[3].innerHTML
                    }
                );

            }

        }

        const ParaEnviar = {
            datos_formulario: datosForm,
            datos_tabla_nuevos: lista_nuevas_profesiones,
            datos_tabla_eliminar: []
        };

        //console.log(ParaEnviar);
        return ParaEnviar;

    }

    async guardarFormulario() {

        const datos = this.recuperaDatosFormulario();

        // Enviamos al servidor.
        try {

            const res = await fetch('http://localhost:5000/formulario_adicional/guardar_formulario', {

                method: 'POST',
                headers: {

                    'Accept': 'application/json',
                    'Content-Type': 'application/json'

                },
                body: JSON.stringify(datos)

            });

            const data = await res.json();

            //console.log(data);
            if(data.guardado === true) {

                let v = mensajeNormal("Éxito", "Se han guardado los datos");
                v.open();

            }


        } catch (error) {
            console.error(error);
        }

    }

    limpiarFormulario() {

       
        const arrayItems = [
            "cbo_nacionalidad", "txt_lugarnac", "txt_alergia", "cbo_tiposangre", "txt_capacidades"
        ];

        arrayItems.filter(valor => {
            return document.getElementById(valor).value = "";
        });
                
    }

}

function camposNoValidos(estado) {

    let adi = new FormAdicionalUI();

    if (estado === true) {
        adi.puesto.className = "is-invalid form-control form-control-sm";
        adi.lugartrabajo.className = "is-invalid form-control form-control-sm";
        adi.puesto.focus();
    } else {
        adi.puesto.className = "form-control form-control-sm";
        adi.lugartrabajo.className = "form-control form-control-sm";
    }

}