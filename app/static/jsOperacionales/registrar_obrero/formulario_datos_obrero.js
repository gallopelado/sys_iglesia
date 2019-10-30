import {autoCompletar} from '../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {
    const idpostulacion = document.getElementById('idpostulacion').value;
    
    window.obtenerCalificados = async(idpostulacion) => {
        try {
            const res = await fetch(`/membresia/registrar_obrero/traer_calificados/${idpostulacion}`);
            const data = await res.json();
            console.log(data);
            autoCompletar(data, 'miembro', 'idmiembro', 'idobrero', 'obrero');
            return data;
        } catch (error) {
            console.error(error);
        }
    }
    obtenerCalificados(idpostulacion);    
});