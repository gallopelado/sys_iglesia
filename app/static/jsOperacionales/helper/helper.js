/**
 * Este fichero pretende incluir todas aquellas funciones genericas.
 * 
 * @author <juanftp100@gmail.com> Juan Jose Gonzalez Ramirez
 */

/**
 * Funcion hacerDataTable()
 * 
 * Convierte todos los datos cargados una tabla
 * al formato de DataTable.
 * 
 */
function hacerDataTable(id) {
    $(`#${id}`).DataTable({
        'destroy': true,
        "lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "Todos"]],
        "language": idioma_spanish
    });
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
function mensajeConfirmacion(titulo, contenido, fn) {
    /* $.confirm({
         theme: 'supervan',
         title: titulo,
         content: contenido,
         buttons: {
             Si: {
                 text: 'Si',
                 btnClass: 'btn-blue',                
                 action: function() {
 
                 }
                 
             },
             No: {
                 text: 'No',
                 btnClass: 'btn-red',                
                 action: function(){
                     
                 }
             }
         }
     });*/
    let confirm = $.confirm({
        lazyOpen: true,
        theme: 'supervan',
        title: titulo,
        content: contenido,
        buttons: {
            Si: {
                text: 'Si',
                btnClass: 'btn-blue',
                action: function () {
                    console.log('Si, ejecutando');
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
    return confirm;
}