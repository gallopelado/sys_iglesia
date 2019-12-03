/**
 * Archivo encargado de controlar el index
 * 
 */
document.addEventListener('DOMContentLoaded', () => {

    const getActividades = async () => {
        const anho = document.getElementById('cbm_anho').value;
        try {
            const res = await fetch(`/actividades/registrar_actividades_anuales/get_actividades_json/${anho}`);
            const data = await res.json();
            return data;
        } catch (error) {
            console.error(error);
        }
    }

    const cargarTabla = async() => {
        const tbody = document.getElementById('tb_actividades');
        const botonModificar = `<a href="" class="btn btn-sm btn-primary">Modificar</a>`;
        const botonEliminar = `<a href="" class="btn btn-sm btn-danger">Eliminar</a>`;
        let datos = '';
        const lista_acti = await getActividades();
        console.log(lista_acti);
        for(let d of lista_acti) {
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
    }

    cargarTabla();

});