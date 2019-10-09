export default class ListaCandidato {

    /**
     * Método traerPostulaciones
     * 
     * Obtiene las postulaciones según parámetro. 
     * ABIERTA, CERRADA, ANULADA.
     * 
     * @param {*} opcion 
     * @returns {json} data
     */
    async traerPostulaciones(opcion = 'TODAS') {

        try {

            const res = await fetch(`/membresia/registrar_candidatos/traer_postulaciones/${opcion}`);
            const data = await res.json();

            return data;

        } catch (error) {
            console.error(error);
        }

    }


    /**
     * Método cargarTabla.
     * 
     * Procesa el resultado de las postulaciones en para salida en una
     * tabla HTML.
     * 
     * @param {*} opcion 
     */
    async cargarTabla(opcion = 'TODAS') {

        const tb = document.getElementById('tb_postulaciones');

        try {

            const data = await this.traerPostulaciones(opcion);
            let cadenas = '';

            if (data !== undefined && data.length > 0) {

                for (let indice in data) {

                    if (data[indice][2] === 'ABIERTA') {

                        cadenas += `
                    
                            <tr id="${data[indice][0]}">
                                <td>${data[indice][1]}</td>
                                <td>${data[indice][2]}</td>
                                <td class="">
                                    <div class="table-data-feature">

                                        <a href="" class="item btn btn-primary" data-toggle="modal" data-placement="top"
                                            title="Ver">
                                            <i class="zmdi zmdi-mail-send"></i>
                                        </a>

                                        <a href="/membresia/registrar_candidatos/asignar_candidatos/${data[indice][0]}"
                                            class="item btn btn-warning" data-toggle="tooltip" data-placement="top"
                                                title="Asignar">
                                                <i class="zmdi zmdi-edit"></i>
                                        </a>

                                    </div>
                                </td>
                            </tr>
                    
                        `;
                    } else {
                        cadenas += `
                    
                            <tr id="${data[indice][0]}">
                                <td>${data[indice][1]}</td>
                                <td>${data[indice][2]}</td>
                                <td><span class="badge badge-default">No Editable</span></td>
                            </tr>
                    
                        `;
                    }
                }
                tb.innerHTML = '';
                tb.innerHTML = cadenas;

            } else {
                console.error('Error al traer postulaciones');
            }

        } catch (error) {
            console.log(error);
        }

    }

}