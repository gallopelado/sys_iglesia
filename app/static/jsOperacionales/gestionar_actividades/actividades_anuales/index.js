/**
 * Archivo encargado de controlar el index
 * 
 */
import { idioma_spanish } from '../../helper/helper.js';
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
        const botonModificar = `<a href="" class="btn btn-sm btn-primary">Modificar</a>`;
        const botonEliminar = `<a href="" class="btn btn-sm btn-danger">Eliminar</a>`;
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
                            ${botonModificar} ${botonEliminar}
                        </div>
                        </td>
                    </tr>
                `;
            }
            tbody.innerHTML = datos;
            $('#tabla_actividades').DataTable({
                "language": idioma_spanish,
                "destroy": true
            });
        }
    }

    window.nuevaActividad = () => {
        const idanho = document.getElementById('cbm_anho').value;
        location.href = `/actividades/registrar_actividades_anuales/form_actividad/${idanho}`;
    }

    cargarTabla(anho);
    comboAnho.addEventListener('change', () => {
        const anho = comboAnho.value;
        const tbody = document.getElementById('tb_actividades');
        tbody.innerHTML = '';        
        cargarTabla(anho);
    });
});