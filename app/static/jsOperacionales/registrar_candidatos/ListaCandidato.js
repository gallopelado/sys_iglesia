import {autoCompletar} from '../helper/helper.js';

export default class ListaCandidato {

    constructor() {

        this.idpostulacion = document.getElementById('idpostulacion');
        this.idcandidato = document.getElementById('idcandidato');
        this.txt_candidato = document.getElementById('txt_candidato');
        this.tabla = document.getElementById('tabla_detalle');
        this.tb = document.getElementById('tb_detalle');
        this.btnGuardar = document.getElementById('btnGuardar');
        this.btnCancelar = document.getElementById('btnCancelar');

    }

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


    async traerDetalle() {

        const idpostulacion = document.getElementById('idpostulacion').value;
        try {
            
            const res = await fetch(`/membresia/registrar_candidatos/traer_detalle_candidatos/${idpostulacion}`);
            const data = await res.json()
            
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

                                        <a href="/membresia/registrar_candidatos/ver_candidatos/${data[indice][0]}" 
                                            class="item btn btn-primary" data-toggle="modal" data-placement="top"
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
                    } else if (data[indice][2] === 'CERRADA') {
                        cadenas += `
                    
                            <tr id="${data[indice][0]}">
                                <td>${data[indice][1]}</td>
                                <td>${data[indice][2]}</td>
                                <td>
                                    <div class="table-data-feature">

                                        <a href="/membresia/ver_candidatos/asignar_candidatos/${data[indice][0]}" 
                                            class="item btn btn-primary" data-toggle="modal" data-placement="top"
                                            title="Ver">
                                            <i class="zmdi zmdi-mail-send"></i>
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


    async cargarCandidatos() {

        try {
            
            const res = await fetch('/membresia/registrar_candidatos/traer_candidatos');
            const data = await res.json()
            
            autoCompletar(data, 'persona', 'idmiembro', 'idcandidato', 'txt_candidato');

        } catch (error) {
            console.error(error);
        }

    }


    agregarFila() {

        const tabla = this.tb;
        const bteliminar = `
        <div class="table-data-feature">
        <button type="button" onclick="eliminarFila(this.parentElement.parentElement.parentElement)" class="item btn btn-warning"
        data-toggle="tooltip" data-placement="top" title="Borrar">
        <i class="zmdi zmdi-delete"></i>
        </button></div>`;
         
        if (this.verificaRepetidos()) {

            const row = tabla.insertRow();
            const col1 = row.insertCell();
            const col2 = row.insertCell();
            const col3 = row.insertCell();
            
            row.id = this.idcandidato.value;
            col1.innerHTML = this.txt_candidato.value;
            col2.innerHTML = '<span class="badge badge-default">En breve</span>';
            col3.innerHTML = bteliminar;

        }
        
    }

    /**
     * Método eliminarFila.
     * 
     * Solamente elimina la fila de la tabla según el índice html.
     * 
     * @param {*} b 
     */
    eliminarFila(b) {

        console.log(b);

    }


    /**
     * Método eliminarCandidato.
     * 
     * Elimina el registro candidato de la base de datos.
     * 
     * @param {*} idcandidato 
     */
    async eliminarCandidato(idpostulacion, idcandidato) {

        const datos = {
            idpostulacion: idpostulacion,
            idcandidato, idcandidato
        }

        try {
            
            const res = await fetch('/membresia/registrar_candidatos/eliminar_candidato', {
                method: 'PUT'
                , headers: {
                    'Content-Type': 'application/json'
                }
                , body: JSON.stringify(datos)
            });
            const data = await res.json()

            console.log(data);

        } catch (error) {
            console.error(error);
        }


    }


    verificaRepetidos() {

        const tb = this.tb.rows;
        let tr;
        
        if (tb.length > 0) {

            for (let i=0; i <= tb.length-1; i++) {
                
                tr = tb[i];                
                if( tr.children.length > 0) {
                    
                    if (tr.id == this.idcandidato.value) {
                        alert('Repetido');
                        return false;
                    }

                }

            }

        }

        return true;

    }
}