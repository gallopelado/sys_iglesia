document.addEventListener('DOMContentLoaded', () => {

    window.modificar = (idcomite) => {
        const conf = confirm('Desea modificarlo?');
        if (conf) {
            location.href = `/membresia/registrar_comite/formulario/${idcomite}`;
        }
    }

    window.baja = (idcomite) => {
        const conf = confirm('Desea dar de baja?');
        if (conf) {
            
        }
    }


});