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
        let botonConfirmar = (id) => '<button type="button" class="btn btn-success btn-sm m-l-10 m-b-10">Procesado</button>';
        let botonModificar = (id) => '';
        let botonEliminar  = (id) => '';
        if (estado == 'NO-CONFIRMADO') {
            botonConfirmar = (id) => `<button type="button" class="btn btn-sm btn-success" onclick="confirmar(${id})">Confirmar</button>`;
            botonModificar = (id) => `<button type="button" class="btn btn-sm btn-primary" onclick="modificar(${id})">Modificar</button>`;
            botonEliminar = (id) => `<button type="button" class="btn btn-sm btn-danger" onclick="eliminar(${id})">Cancelar</button>`;
        }
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
                            ${botonConfirmar(d.idreserva)}
                        </td>
                        <td>
                        <div class="table-data-feature">                     
                            ${botonModificar(d.idreserva)} ${botonEliminar(d.idreserva)}
                        </div>
                        </td>
                    </tr>
                `;
            }
            tbody.innerHTML = "";
            tbody.innerHTML = datos;                        
            /*let tab = $('#tabla_reserva').DataTable({
                "language": idioma_spanish,
                "destroy": true
            });*/
            //tab.clear();
            //tbody.innerHTML = datos; 
            //$('#tabla_reserva').DataTable();           
        }
    }

    window.nuevaReserva = async() => {                        
        location.href = `/actividades/registrar_reserva/form_reserva/${anho}`;        
    }

    cargarTabla(estado);
    comboEstado.addEventListener('change', () => {
        const estado = comboEstado.value;
        const tbody = document.getElementById('tb_reserva');
        tbody.innerHTML = '';        
        cargarTabla(estado);
    });

    window.modificar = (id) => {                
        const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/registrar_reserva/form_reserva/${id}`;
        }
        m.open();
    }

    window.eliminar = (id) => {                
        const m = mensajeConfirmacion('Confirmar', 'Desea cancelar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/registrar_reserva/eliminar/${id}`;
        }
        m.open();
    }

    window.confirmar = (id) => {                
        const m = mensajeConfirmacion('Confirmar', 'Desea confirmar reserva ?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/generar_contrato/formulario_contrato`;
        }
        m.open();
    }
});