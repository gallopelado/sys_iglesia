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
function mensaje(titulo, contenido, url) {
    $.confirm({
        theme: 'supervan',
        title: titulo,
        content: contenido,
        buttons: {
            Si: {
                text: 'Si',
                btnClass: 'btn-blue',                
                action: function(){
                    window.location.href = url;
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
function modificar(url) {
    mensaje('Mensaje de Confirmacion!', 'Desea Modificar?', url);    
}
/**
 * Funcion eliminar()
 * 
 * Llama a la funcion mensaje() con un mensaje personalizado, realiza redireccion de pagina al 
 * controlado por medio de su metodo, en este caso eliminar de ciudad.
 * 
 * @param {*} id 
 */
function eliminar(url) {
    mensaje('Mensaje de Confirmacion!', 'Desea Eliminar?', url);    
}