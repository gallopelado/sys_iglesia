import {mensajeConfirmacion} from '../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {
    
    window.modificar = (url) => {
        const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
        m.buttons.Si.action = () => {                
            location.href = `${url}`;
        }
        m.open();
    }
    window.eliminar = (url) => {
        const m = mensajeConfirmacion('Confirmar', 'Desea eliminar?');
        m.buttons.Si.action = () => {                
            location.href = `${url}`;
        }
        m.open();
    }
});