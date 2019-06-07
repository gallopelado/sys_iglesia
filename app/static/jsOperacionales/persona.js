$(function() {
    hacerDataTable();    
});

/**
 * Funcion hacerDataTable()
 * 
 * Convierte todos los datos cargados una tabla
 * al formato de DataTable.
 * 
 */
function hacerDataTable() {
    $('#tabla_persona').DataTable({
        'destroy': true,
        "lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "Todos"]],
        "language":idioma_spanish        
    });
}

/**
 * Funcion iniciarModal.
 * 
 * Obtiene datos del modelo Persona como objeto, 
 * carga dichos datos en el objeto modal para mostrar en pantalla.
 * 
 * Tipo: Asincrona.
 * 
 * @param {*} idpersona 
 */
async function iniciarModal(idpersona) {
       
    let data = await obtenerDatosPersona(idpersona);        
    let modal = new ModalPersona();
    modal.cedula.value = data.cedula;
    modal.tipopersona.value = data.tipopersona;
    modal.nombres.value = data.nombres;
    modal.apellidos.value = data.apellidos;
    modal.obs.value = data.obs;
    $('#mediumModal').modal();
        
}

/**
 * Funcion obtenerDatosPersona
 * 
 * Tipo: Asincrona.
 * 
 * Obtiene datos del modelo a traves de fetch, obtiene el objeto response,
 * crea una instancia de Persona para cargar datos.
 * 
 * @param {*} idpersona 
 * @returns {object} persona
 */
async function obtenerDatosPersona(idpersona) {
    
    try {
        const res = await fetch('http://localhost:5000/persona/get_persona/' + idpersona);
        const data = await res.json();
        let persona = new Persona(idpersona, data[1], data[4], data[2], data[3], data[5]);                
        return persona;
    }
    catch (error) {
        return console.error(error);
    } 
    
}

/**
 * Clase Persona.
 * 
 * Definicion de la clase persona.
 * 
 * @author <juanftp100@gmail.com> Juan Gonzalez
 */
class Persona {
    
    /**
     * Constructor de la Clase Persona.
     * 
     * Puede generarse una instancia sin parametros.
     * 
     * @param {*} idpersona 
     * @param {*} cedula 
     * @param {*} tipopersona 
     * @param {*} nombres 
     * @param {*} apellidos 
     * @param {*} obs 
     * 
     */
    constructor(idpersona, cedula, tipopersona, nombres, apellidos, obs) {
        this.idpersona = idpersona;
        this.cedula = cedula;
        this.tipopersona = tipopersona;
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.obs = obs;
    }
}

/**
 * Clase ModalPersona.
 * 
 * Definicion de la clase ModalPersona,
 * se obtiene el node de los elementos en el constructor.
 * 
 * @author <juanftp100@gmail.com> Juan Gonzalez
 */
class ModalPersona {

    /**
     * Constructor de la Clase ModalPersona
     * 
     * Puede generarse una instancia vacia.
     * 
     */
    constructor() {
        this.cedula = document.getElementById('txtcedula');
        this.tipopersona = document.getElementById('cbo_tipopersona');
        this.nombres = document.getElementById('txtnombres');
        this.apellidos = document.getElementById('txtapellidos');
        this.obs = document.getElementById('txtobs');
    }

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
function mensaje(titulo, contenido, url, id) {
    $.confirm({
        theme: 'supervan',
        title: titulo,
        content: contenido,
        buttons: {
            Si: {
                text: 'Si',
                btnClass: 'btn-blue',                
                action: function(){
                    window.location.href = url + id;
                }
            },
            No: {
                text: 'No',
                btnClass: 'btn-red',                
                action: function(){
                    
                }
            }
        }
    });
}

/**
 * Funcion modificar()
 * 
 * Llama a la funcion mensaje() con un mensaje personalizado, realiza redireccion de pagina al 
 * controlado por medio de su metodo, en este caso modificar.
 * 
 * @param {*} id 
 */
function modificar(id) {
    mensaje('Mensaje de Confirmacion!', 'Desea Modificar?', 'http://localhost:5000/persona/modificar/', id);    
}
/**
 * Funcion eliminar()
 * 
 * Llama a la funcion mensaje() con un mensaje personalizado, realiza redireccion de pagina al 
 * controlado por medio de su metodo, en este caso eliminar.
 * 
 * @param {*} id 
 */
function eliminar(id) {
    mensaje('Mensaje de Confirmacion!', 'Desea Eliminar?', 'http://localhost:5000/persona/eliminar/', id);    
}


/**
 * Variable idioma_spanish
 * 
 * Se define la traduccion para el DataTable.
 * 
 */
var idioma_spanish = {
    "sProcessing": "Procesando...",
    "sLengthMenu": "Mostrar _MENU_ registros",
    "sZeroRecords": "No se encontraron resultados",
    "sEmptyTable": "Ningún dato disponible en esta tabla",
    "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
    "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
    "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
    "sInfoPostFix": "",
    "sSearch": "Buscar:",
    "sUrl": "",
    "sInfoThousands": ",",
    "sLoadingRecords": "Cargando...",
    "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
    },
    "oAria": {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
    }
}