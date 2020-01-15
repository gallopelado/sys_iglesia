/**
 * Archivo encargado de controlar el index
 * 
 */
import { idioma_spanish, mensajeConfirmacion } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {

    const comboAnho = document.getElementById('cbm_anho');
    const anho = comboAnho.value;
    const getActividades = async (anho) => {
        try {
            const res = await fetch(`/actividades/registrar_actividades_anuales/get_actividades_json/${anho}`);
            const data = await res.json();
            return data;
        } catch (error) {
            console.error(error);
        }
    }

    const cargarTabla = async (anho) => {
        const tbody = document.getElementById('tb_actividades');
        const botonModificar = (idactividad) => `<button type="button" class="btn btn-sm btn-primary" onclick="modificar(${idactividad})">Modificar</button>`;
        const botonEliminar = (idactividad) => `<button type="button" class="btn btn-sm btn-danger" onclick="eliminar(${idactividad})">Eliminar</button>`;
        let datos = '';
        const lista_acti = await getActividades(anho);                
        if (lista_acti != null) {
            for (let d of lista_acti) {
                datos += `
                    <tr>
                        <td>${d.evento}</td>
                        <td>${d.fechainicio}</td>
                        <td>${d.fechafin}</td>
                        <td>
                        <div class="table-data-feature">                     
                            ${botonModificar(d.idactividad)} ${botonEliminar(d.idactividad)}
                        </div>
                        </td>
                    </tr>
                `;
            }                        
            const tab = $('#tabla_actividades').DataTable({
                "language": idioma_spanish,
                "destroy": true
            });
            tab.clear();
            tbody.innerHTML = datos;
        }
    }

    window.nuevaReserva = async() => {                        
        location.href = `/actividades/registrar_reserva/form_reserva/${anho}`;        
    }

    const verificaAnho = async(anho) => {
        try {
            const res = await fetch(`/actividades/registrar_actividades_anuales/verificarAnho/${anho}`)
            const data = await res.json();
            return data;
        } catch (error) {
            console.error(error);
        }
    }

    cargarTabla(anho);
    comboAnho.addEventListener('change', () => {
        const anho = comboAnho.value;
        const tbody = document.getElementById('tb_actividades');
        tbody.innerHTML = '';        
        cargarTabla(anho);
    });

    window.modificar = (idactividad) => {        
        const anho = document.getElementById('cbm_anho').value;
        const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/registrar_actividades_anuales/form_actividad/modificar/${anho}/${idactividad}`;
        }
        m.open();
    }

    window.eliminar = (idactividad) => {        
        const anho = document.getElementById('cbm_anho').value;
        const m = mensajeConfirmacion('Confirmar', 'Desea eliminar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/registrar_actividades_anuales/eliminar/${anho}/${idactividad}`;
        }
        m.open();
    }
});