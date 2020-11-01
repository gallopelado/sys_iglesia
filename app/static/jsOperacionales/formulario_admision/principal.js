document.addEventListener('DOMContentLoaded', () => {

    let ad = new AdmisionPrincipalUI();
    ad.convertirFecha();
    ad.formatearTabla();

});

// Botones
var btnProceder = document.getElementById('btnProceder');
btnProceder.addEventListener('click', () => {

    let m = new ModalBaja()
    m.eliminar();

});

// Funciones para los botones.
function eliminar(id) {

    confirmaBorrar('Mensaje de confirmación', 'Dar de baja?', id);

}

function modificar(id) {
    localStorage.clear();
    let ad = new AdmisionPrincipalUI();
    ad.modificar(id);
}

/**
 * Funcion mensaje
 * 
 * Sirve para mostrar mensaje en pantalla, mensajes de confirmacion.
 * 
 * @param {*} titulo 
 * @param {*} contenido 
 * @param {*} url 
 * @param {*} id 
 */
async function confirmaBorrar(titulo, contenido, id) {

    // Recuperar info para el modal
    let ad = new ModalBaja(),
        data = await ad.obtenerDatos(id);

    $.confirm({
        theme: 'supervan',
        title: titulo,
        content: contenido,
        buttons: {
            Si: {
                text: 'Si',
                btnClass: 'btn-blue',
                action: function () {

                    // Setea campos del modal.
                    ad.idpersona.value = data.encontrado[0];
                    ad.txt_persona.value = data.encontrado[1];

                    // Muestra el modal para la baja.
                    $('#modal_baja').modal();

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

/**
 * Clase ModalBaja.
 * 
 * Contiene definiciones para gestionar el modal de Dar de baja de la persona.
 * 
 *  @author <juanftp100@gmail.com> Juan Jose Gonzalez.
 */
class ModalBaja {

    /**
     * Metodo constructor de la clase ModalBaja.
     * 
     * Se recopila los objetos y sus propiedades de dicho elemento.
     * 
     */
    constructor() {
        this.idpersona = document.getElementById('idadmision'),
            this.txt_persona = document.getElementById('txt_persona'),
            this.chk_disciplina = document.getElementById('chk_disciplina'),
            this.chk_defuncion = document.getElementById('chk_defuncion'),
            this.chk_excomunion = document.getElementById('chk_excomunion'),
            this.chk_traslado = document.getElementById('chk_traslado'),
            this.chk_otras = document.getElementById('chk_otras'),
            this.txtobs = document.getElementById('txtobs');
    }

    /**
     * Metodo obtenerDatos.
     * 
     * Obtiene registros en formato JSON segun el idadmision enviado.(ASINCRONA)
     * 
     * @param {*} id 
     * @returns {json} datos
     */
    async obtenerDatos(id) {

        let data = {
            idadmision: id
        }

        try {

            const res = await fetch('/formulario_admision/obtener_datos_modal', {
                method: 'POST',
                headers: {
                    'Accept': 'applications/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const datos = await res.json()

            return datos;

        } catch (error) {

            console.error(error);
            return false;
        }

    }

    /**
     * Metodo eliminar.
     * 
     * Envia datos tipo json al controlador.(ASINCRONA)
     * 
     */
    async eliminar() {

        let datos = this.obtenerDatosFormulario();

        try {

            const res = await fetch('/formulario_admision/dar_de_baja', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });

            const data = await res.json();
            if (data.cambiado === true) {

                $('#modal_baja').modal('toggle');
                // Refresca la tabla
                let adp = new AdmisionPrincipalUI();
                adp.convertirFecha();


            } else {
                console.error(data);
            }

            console.log(data);

        } catch (error) {
            console.error(error);
        }

    }

    obtenerDatosFormulario() {

        let datos, radioElegido, radios = [
            "chk_disciplina",
            "chk_defuncion",
            "chk_excomunion",
            "chk_traslado",
            "chk_otras"
        ];

        // Recorrer el array en busca del elemento elegido.
        for (let i = 0; i < radios.length; i++) {

            if (document.getElementById(radios[i]).checked === true) {

                radioElegido = radios[i];

                switch (radioElegido) {

                    case "chk_disciplina":

                        radioElegido = "DISCIPLINA";
                        break;

                    case "chk_defuncion":

                        radioElegido = "DEFUNCION";
                        break;

                    case "chk_excomunion":

                        radioElegido = "EXCOMUNION";
                        break;

                    case "chk_traslado":

                        radioElegido = "TRASLADO";
                        break;

                    case "chk_otras":

                        radioElegido = "OTRAS";
                        break;

                }

            }

        }

        // Preparar el objeto json.
        datos = {
            idadmision: this.idpersona.value,
            razonbaja: radioElegido,
            obs: this.txtobs.value.trim() !== '' ? this.txtobs.value : null
        }

        return datos;
    }

}


// Clase principal de la pantalla.
/**
 * Clase AdmisionPrincipalUI.
 * 
 * Contiene definiciones para gestionar la primera vista,
 * en donde se muestra la grilla.
 * 
 * @author <juanftp100@gmail.com> Juan Jose Gonzalez.
 */
class AdmisionPrincipalUI {

    /**
     * Metodo obtenerAdmision().
     * 
     * Obtiene registros del modelo en formato json.
     * 
     */
    async obtenerAdmision() {

        try {

            const res = await fetch('/formulario_admision/lista_admision');
            const data = await res.json()

            return data;

        } catch (error) {
            console.error(error)
        }

    }

    /**
     * Metodo convertirFecha().
     * 
     * Genera filas en la tabla principal con las fechas en formato natural.
     * 
     * 
     */
    async convertirFecha() {

        let cadena = '', data = await this.obtenerAdmision();

        if (data.length > 0) {

            // Setea a idioma spanish
            moment.locale('es');
            for (let i = 0; i < data.length; i++) {

                cadena += `
            <tr>
                <td>
                    ${data[i][1]}</td><td>${data[i][2]}
                </td>
                <td>
                    ${moment(data[i][3]).format('LL')}
                </td>
                <td>
                    <div class="table-data-feature">
                        <button onclick="modificar(${data[i][0]})" class="item btn btn-warning modificar"
                            data-toggle="tooltip" data-placement="top" title="Modificar">
                            <i class="zmdi zmdi-edit"></i>
                        </button>
                        <button onclick="eliminar(${data[i][0]})" class="item btn btn-danger"
                            data-toggle="tooltip" data-placement="top" title="Dar de baja">
                            <i class="zmdi zmdi-delete"></i>
                        </button>
                    </div>
                </td>
            </tr>`;


            }

        } else {

            cadena = "No hay elementos";

        }


        document.getElementById('tb_formadmi').innerHTML = cadena;
    }

    /**
     * Metodo formatearTabla().
     * 
     * Activa el campo de busqueda para filtrar filas.
     * 
     */
    formatearTabla() {

        $("#txtbusqueda").on("keyup", function () {
            var value = $(this).val().toLowerCase();
            $("#tb_formadmi tr").filter(function () {
                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });

    }

    modificar(id) {

        $.confirm({
            theme: 'supervan',
            title: 'Mensaje de confirmación',
            content: 'Desea modificar este registro ?',
            buttons: {
                Si: {
                    text: 'Si',
                    btnClass: 'btn-blue',
                    action: function () {

                        //console.log(`El id es ${id}`);
                        let ad = new AdmisionPrincipalUI();
                        //ad.procesarDatos(id);
                        ad.redireccionarFormulario(id);
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

    redireccionarFormulario(id) {
        window.location.href = `/formulario_admision/frm_modificar/${id}`
    }

}
