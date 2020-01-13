import {mensajeConfirmacion} from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {
    const btnModificar = document.getElementById('btnModificar');
    const btnEliminar = document.getElementById('btnEliminar');
        
   
    window.modificar = (url) => {
        const mc = mensajeConfirmacion('Mensaje', 'Desea modificar');
        mc.buttons.Si.action = () => {
            location.href = url;
        }
        mc.open();
    }
    window.eliminar = (url) => {
        const mc = mensajeConfirmacion('Mensaje', 'Desea eliminar');
        mc.buttons.Si.action = () => {
            location.href = url;
        }
        mc.open();
    }
    window.ver = (url) => {
        location.href = url;        
    }
});
