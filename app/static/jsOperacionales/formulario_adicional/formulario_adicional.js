import { obtenerIdUrl, mensajeConfirmacion, mensajeNormal } from '../helper/helper.js';
import ModalProfesion from './ModalProfesion.js';
import FormAdicionalUI from './FormAdicionalUI.js';

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
/**
 * Funcion global eliminarFila.
 * 
 * Según instancia de FormAdicionalUi,
 * una vez generado el historial de profesiones,
 * se utiliza esta funcion para eliminar fila, de 
 * dicha tabla.
 * 
 */
window.eliminarFila = function () {    
    const adi = new FormAdicionalUI();
    adi.eliminarFila();
}

/**
 * Funcion global camposNoValidos.
 * 
 * Según instancia de FormAdicionalUi,
 * se cambian estilos de colores en el elemento.
 * Inválido de color rojo, azul para normal.
 * 
 */
window.camposNoValidos = function(estado) {

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