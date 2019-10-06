import { autoCompletar,mensajeNormal } from '../helper/helper.js';

export default class FormularioDocumentos {

    constructor() {

        this.idtipodocumento = document.getElementById('idtipodocumento');
        this.txt_tipodocumento = document.getElementById('txt_tipodocumento');
        this.txt_fecha = document.getElementById('txt_fecha');
        this.idmiembro = document.getElementById('idmiembro');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.idconyuge = document.getElementById('idconyuge');
        this.txt_conyuge = document.getElementById('txt_conyuge');
        this.txt_oficiador = document.getElementById('txt_oficiador');
        this.txt_documento = document.getElementById('txt_documento');
        this.txt_declaracion = document.getElementById('txt_declaracion');
        this.txt_notas = document.getElementById('txt_notas');
        this.txt_testigo1 = document.getElementById('txt_testigo1');
        this.txt_testigo2 = document.getElementById('txt_testigo2');
        this.btnGuardar = document.getElementById('btnGuardar');
        this.btnCancelar = document.getElementById('btnCancelar');

    }

    async cargarTiposDocumentos() {

        const d = await this.getTiposDocumentos();

        //console.log(d[0][0]);

        autoCompletar(d[0][0], 'documento', 'iddocumento', 'idtipodocumento', 'txt_tipodocumento');

    }

    async getTiposDocumentos() {

        try {

            const res = await fetch('http://localhost:5000/documentos_miembro/lista_tipodocumentos');
            const data = await res.json();

            return data

        } catch (error) {
            console.error(error);
        }

    }

    async getPersonas() {

        try {

            const res = await fetch('http://localhost:5000/documentos_miembro/lista_personas_json');
            const data = await res.json();

            return data;

        } catch (error) {
            console.error(error);
        }

    }

    async cargarPersonas() {

        const personas = await this.getPersonas();

        autoCompletar(personas[0][0], 'persona', 'idpersona', 'idmiembro', 'txt_miembro');

        // Conyuge
        autoCompletar(personas[0][0], 'persona', 'idpersona', 'idconyuge', 'txt_conyuge');

    }

    cargarFormulario() {

        const solicitud = indexedDB.open('db_documentos', 1);
        let bd;

        solicitud.onsuccess = (e) => {

            bd = solicitud.result;

            const transaccion = bd.transaction(['documentos_miembro']);
            const documentoStore = transaccion.objectStore('documentos_miembro');
            const request = documentoStore.getAll();
            request.onsuccess = (e) => {
                const datos = e.target.result[0];
                //console.log(datos);
                document.getElementById('id_antiguo_tipodocumento').value = datos.idtipodocumento;
                this.idtipodocumento.value = datos.idtipodocumento;
                this.txt_tipodocumento.value = datos.documento;
                this.txt_fecha.value = datos.fechadocumento;
                this.idmiembro.value = datos.idmiembro;
                this.txt_miembro.value = datos.persona;
                this.idconyuge.value = datos.conyuge_id;
                this.txt_conyuge.value = datos.conyuge;
                this.txt_oficiador.value = datos.oficiador;
                document.getElementById('txt_nombredocumento').innerHTML = `
                
                    <div class="card-header bg-secondary">
                        <strong class="card-title text-light">Nombre del documento guardado.</strong>
                    </div>
                    <div class="card-body text-white bg-primary">
                        <p class="card-text text-light">
                            <fa class="fa fa-file"></fa>
                            documento_${datos.archivo}
                        </p>
                    </div>

                `;
                this.txt_declaracion.value = datos.declaracion;
                this.txt_notas.value = datos.notas;
                this.txt_testigo1.value = datos.testigo1;
                this.txt_testigo2.value = datos.testigo2;
            }
            bd.close();

        }

    }

    recuperarDatosFormulario() {

        // Crear objeto FormData.
        const frm = new FormData();

        // Sanear variables.
        let id_antiguo_tipodocumento = document.getElementById('id_antiguo_tipodocumento') === null ? null : document.getElementById('id_antiguo_tipodocumento').value;
        let idtipodocumento = this.idtipodocumento.value;
        let descridocumento = this.txt_tipodocumento.value;
        let txt_fecha = this.txt_fecha.value;
        let idmiembro = this.idmiembro.value;
        let miembro = this.txt_miembro.value.trim();
        let idconyuge = this.idconyuge.value;
        let txt_conyuge = this.txt_conyuge.value.trim();
        let oficiador = this.txt_oficiador.value.trim();
        //let documento = this.txt_documento;
        let declaracion = this.txt_declaracion.value.trim();
        let notas = this.txt_notas.value.trim();
        let testigo1 = this.txt_testigo1.value.trim();
        let testigo2 = this.txt_testigo2.value.trim();



        // Validar
        if (!descridocumento) {
            alert('El campo tipo documento no puede estar vacío o no válido');
            this.txt_tipodocumento.focus();
            return false;
        }

        if (!txt_fecha) {
            alert('El campo fecha no puede estar vacía.');
            this.txt_fecha.focus();
            return false;
        }

        if (!miembro) {
            alert('El campo miembro no es válido');
            this.txt_miembro.focus();
            return false;
        }

        if (!oficiador) {
            alert('El campo oficiador no debe quedar vacío');
            this.txt_oficiador.focus();
            return false;
        }

        if (!declaracion) {
            alert('El campo declaracion no debe quedar vacío');
            this.txt_declaracion.focus();
            return false;
        }



        // Validar documento PDF.
        const extensiones_permitidas = ['PDF', 'EPUB'];
        const longitud_extension = extensiones_permitidas.length;
        const peso = 30720; // 30 MB.
        const documento = document.getElementById('txt_documento');
        const objDocumento = documento.files[0];
        console.log(objDocumento);

        // Si no es undefined.
        if (typeof (objDocumento) !== 'undefined') {

            //console.log(objDocumento);

            // Obtener extensión del fichero.
            let extensionFile = objDocumento.type.split('/')[1];
            extensionFile = extensionFile.toUpperCase();

            // Tamaño del documento.
            const tamaDocumento = Math.round(objDocumento.size / 1024);
            let nopermitida = true;

            if (tamaDocumento <= peso) {

                // Recorre en busca de extensiones correctas.

                for (let i = 0; i <= longitud_extension; i++) {

                    if (extensionFile === extensiones_permitidas[i]) {

                        nopermitida = false;
                        const extension_normalizada = extensionFile.toLowerCase();
                        const nuevoNombre_fichero = `${idmiembro}_${idtipodocumento}.${extension_normalizada}`;

                        // Asignar binario al objeto frm.
                        frm.append('documento_binario', objDocumento, nuevoNombre_fichero);
                        frm.append('nombre_binario', nuevoNombre_fichero);
                        break;

                    }
                }

                if (nopermitida) {

                    alert('Solo se admiten documentos en PDF o EPUB');

                }

            } else {

                alert('Tamaño permitido hasta 30 MB');

            }

        } else {

            // No subió ningún documento.
            frm.append('documento_binario', null);
            frm.append('nombre_binario', null);

        }

        // Asignar a FormData el resto.
        frm.append('id_antiguo_tipodocumento', id_antiguo_tipodocumento)
        frm.append('idtipodocumento', idtipodocumento)
        frm.append('txt_fecha', txt_fecha);
        frm.append('idmiembro', idmiembro);
        frm.append('idconyuge', idconyuge);
        frm.append('oficiador', oficiador);
        frm.append('declaracion', (declaracion));
        frm.append('notas', notas);
        frm.append('testigo1', testigo1);
        frm.append('testigo2', testigo2);

        return frm;

    }

    async guardarFormulario() {

        const datosForm = this.recuperarDatosFormulario();

        if (datosForm) {

            try {

                const res = await fetch('http://localhost:5000/documentos_miembro/guardar_formulario', {

                    method: 'POST',
                    body: datosForm

                });
                const data = await res.json();

                if (data.guardado === true) {

                    window.location.href = 'http://localhost:5000/documentos_miembro/';

                } else {
                    //console.error(data);
                    if (!data.guardado) {

                        const m = mensajeNormal('Cuidado!', 'Posiblemente quieres duplicar este registro o ha sido dado de baja');
                        m.open();

                    }
                }

            } catch (error) {

                console.error(error);

            }

        }

    }

    async modificarFormulario() {

        const datosForm = this.recuperarDatosFormulario();

        if (datosForm) {

            try {

                const res = await fetch('http://localhost:5000/documentos_miembro/modificar_formulario', {

                    method: 'POST',
                    body: datosForm

                });
                const data = await res.json();

                if (data.guardado === true) {

                    window.location.href = 'http://localhost:5000/documentos_miembro/';

                } else {
                    //console.error(data);
                    if (!data.guardado) {

                        const m = mensajeNormal('Cuidado!', 'Posiblemente quieres duplicar este registro o ha sido dado de baja');
                        m.open();

                    }
                }

            } catch (error) {

                console.error(error);

            }

        }

    }
    
}
