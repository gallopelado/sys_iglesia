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
    $('#tabla_ciudad').DataTable({
        'destroy': true,
        "lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "Todos"]],
        "language":idioma_spanish        
    });
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
 * controlado por medio de su metodo, en este caso modificar de ciudad.
 * 
 * @param {*} id 
 */
function modificar(id) {
    mensaje('Mensaje de Confirmacion!', 'Desea Modificar?', '/ciudad/modificar/', id);    
}
/**
 * Funcion eliminar()
 * 
 * Llama a la funcion mensaje() con un mensaje personalizado, realiza redireccion de pagina al 
 * controlado por medio de su metodo, en este caso eliminar de ciudad.
 * 
 * @param {*} id 
 */
function eliminar(id) {
    mensaje('Mensaje de Confirmacion!', 'Desea Eliminar?', '/ciudad/eliminar/', id);    
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