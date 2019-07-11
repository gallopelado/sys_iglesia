import { idioma_spanish } from '../helper/helper.js';

export default class PrincipalUI {

    constructor() {
        this.tabla = document.getElementById('tabla_formdocu');
    }

    async cargarTabla() {

        try {

            const res = await fetch('http://localhost:5000/documentos_miembro/lista_miembros_documento');
            const data = await res.json();            
            let matrizResultados = [];
            const longitud_data = data.length;
            

            if (longitud_data > 0) {

                // Set idioma
                moment.locale('es');

                for (let item of data[0][0]) {
                    
                    matrizResultados.push({
                        documento: item.documento,
                        persona: item.persona,
                        fecha: moment(item.fechadocumento).format('LL'),
                        acciones: `
                            <td>
                            
                                <div class="table-data-feature">
                                    <button onclick="ver(${ item.idmiembro}, ${item.idtipodocumento})" class="item btn btn-primary" data-toggle="modal" data-placement="top" title="Ver">
                                            <i class="zmdi zmdi-mail-send"></i>
                                    </button>
                                    <button onclick="modificar( ${ item.idmiembro}, ${item.idtipodocumento} )" class="item btn btn-warning modificar"
                                        data-toggle="tooltip" data-placement="top" title="Modificar">
                                            <i class="zmdi zmdi-edit"></i>
                                    </button>
                                    <button onclick="eliminar( ${ item.idmiembro}, ${item.idtipodocumento} )" class="item btn btn-danger"
                                        data-toggle="tooltip" data-placement="top" title="Dar de baja">
                                            <i class="zmdi zmdi-delete"></i>
                                    </button>
                                </div> 
                            
                            </td>`
                    });
                }

            } else {

                cadena = "No hay datos registrados..";

            }
            // Formatear con DataTable.
            $('#tabla_formdocu').DataTable({
                'destroy': true,
                "lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "Todos"]],
                "language": idioma_spanish,
                data: matrizResultados,
                columns: [
                    { data: 'documento' },
                    { data: 'persona' },
                    { data: 'fecha' },
                    { data: 'acciones' }
                ]
            });                                 

        } catch (error) {
            console.error(error);
        }

    }
    
    async obtenerMiembroDocumento(idmiembro, idtipodocu) {

        const datos = {
            idmiembro: idmiembro,
            idtipodocumento: idtipodocu
        }

        try {
            
            const res = await fetch('http://localhost:5000/documentos_miembro/obtener_miembro_documento', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            return data;

        } catch (error) {
            console.error(error);
        }

    }

    async guardarTemporal(idmiembro, idtipodocu) {
        
        // Se obtienen datos del servidor.
        const miembro = await this.obtenerMiembroDocumento(idmiembro, idtipodocu);        
        
        // Borrar base de datos.
        let borrar = indexedDB.deleteDatabase('db_documentos', 1);
       /* borrar.onsuccess = function() {
            console.log('Se borro la bd');
        }
        borrar.onerror = function() {
            console.error('Ocurrió un error al borrar');
        }
        borrar.onblocked = function () {
            console.error('no se pudo borrar, bd bloqueada');
        }*/

        // Creacion e insercion.
        const dbName = 'db_documentos';
        let bd;
        let solicitud = indexedDB.open(dbName, 1);
        const doc = new PrincipalUI();

        solicitud.onsuccess = function () {                        

            bd = solicitud.result;

            let transaccion = bd.transaction(['documentos_miembro'], 'readwrite');

            let documento = transaccion.objectStore('documentos_miembro');

            documento.add(miembro);                        

            bd.close();
        }

        solicitud.onupgradeneeded = function (e) {

            bd = e.target.result;
            bd.createObjectStore('documentos_miembro', { keyPath: 'idmiembro' });
                                    
        }        
        
    }

    verDatos(idmiembro) {

        const solicitud = indexedDB.open('db_documentos', 1);
        let bd;

        solicitud.onsuccess = () => {

            bd = solicitud.result;
            
            let transaccion = bd.transaction(['documentos_miembro']);
            let documentoStore = transaccion.objectStore('documentos_miembro');
            let request = documentoStore.get(idmiembro);
            request.onsuccess = (e) => {
                console.log(e.target.result);
            }
            request.onerror = function (event) {
                // Handle errors!
                console.error('ocurrio un error');
            };

            bd.close();

        }

    }    

    async eliminarFormulario(idpersona, iddocumento) {

        const datos = {
            idpersona: idpersona,
            iddocumento: iddocumento
        }

        try {

            const res = await fetch('http://localhost:5000/documentos_miembro/eliminar_formulario', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();
            //console.log(data.estado);
            this.cargarTabla();
            return data.estado === true ? data.estado : false;             
            
        } catch (error) {
            console.error(error);
            return false;
        }

    }

    crearModal() {

        let tabla = document.getElementById('tabla_formdocu');
        let longitud_filas = tabla.rows.length;
        console.log(longitud_filas);
       /* for (let i = 1; i < longitud_filas; i++) {

            console.log(tabla.rows);

        }*/

    }
}
