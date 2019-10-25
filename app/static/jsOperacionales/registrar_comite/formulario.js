import { autoCompletar } from '../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {    

    window.cargarMinisterios = async () => {

        try {
            
            const res = await fetch('/membresia/registrar_comite/get_ministerios');
            const data = await res.json()            
            if (data.length > 0) {
                autoCompletar(data, 'descripcion', 'id', 'txt_idcomite', 'txt_comite');
            }

        } catch (error) {
            console.error(error);
        }
        
    }

    window.cargarMiembros = async () => {

        try {
            
            const res = await fetch('/membresia/registrar_comite/get_miembros_perfil');
            const data = await res.json()
            console.log(data);
            if (data.length > 0) {
                autoCompletar(data, 'miembro', 'idmiembro', 'txt_idlider', 'txt_lider');
                autoCompletar(data, 'miembro', 'idmiembro', 'txt_idsuplente', 'txt_suplente');
            }

        } catch (error) {
            console.error(error);
        }
        
    }

    cargarMinisterios();
    cargarMiembros();

});