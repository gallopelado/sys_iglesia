import ModalReincorporacion from './ModalReincorporacion.js';
import ModalBaja from './ModalBaja.js';

document.addEventListener('DOMContentLoaded', () => {

    window.mostrar = async(id) => {

        // instaciar la clase ModalBaja,
        // obtener el nombre del miembro.
        const mb = new ModalBaja();
        const datos = await mb.obtenerDatos(id);

        // Asignar en el formulario.
        const modal = new ModalReincorporacion();
        modal.idpersona.value = datos.encontrado[0];
        modal.txt_persona.value = datos.encontrado[1];                
        
        // Inicia el modal.
        modal.iniciar();

        modal.btnProceder.addEventListener('click', async() => {
            const { procesado } = await modal.reincorporar();
            console.log(procesado);
            if(procesado === true) {
                location.href = '/miembro_oficial/dados_baja';
            }
        });

    }    

});

