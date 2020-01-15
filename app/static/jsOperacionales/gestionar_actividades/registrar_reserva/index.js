/**
 * Archivo encargado de controlar el index
 * 
 */
import { idioma_spanish, mensajeConfirmacion } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {

    const comboEstado = document.getElementById('cbm_estado');    
    let estado = comboEstado.value;
    const getReservas = async (estado) => {
        try {
            const res = await fetch(`/actividades/registrar_reserva/get_reservas_json`, {
                method:'POST',
                headers: {
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({estado:estado})
            });
            const data = await res.json();
            return data;
        } catch (error) {
            console.error(error);
        }
    }

    const cargarTabla = async (estado) => {
        const tbody = document.getElementById('tb_reserva');
        const botonConfirmar = (idactividad) => `<button type="button" class="btn btn-sm btn-success" onclick="modificar(${idactividad})">Confirmar</button>`;
        const botonModificar = (idactividad) => `<button type="button" class="btn btn-sm btn-primary" onclick="modificar(${idactividad})">Modificar</button>`;
        const botonEliminar = (idactividad) => `<button type="button" class="btn btn-sm btn-danger" onclick="eliminar(${idactividad})">Eliminar</button>`;
        let datos = '';
        const lista = await getReservas(estado);                       
        if (lista != null) {
            for (let d of lista) {
                datos += `
                    <tr>
                        <td>${d.actividad}</td>
                        <td>${d.fechainicio}</td>
                        <td>${d.horainicio}</td>
                        <td>
                            ${botonConfirmar(d.idactividad)}
                        </td>
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

    cargarTabla(estado);
    comboEstado.addEventListener('change', () => {
        const estado = comboEstado.value;
        const tbody = document.getElementById('tb_reserva');
        tbody.innerHTML = '';        
        cargarTabla(estado);
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