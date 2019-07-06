class FormularioDocumentos {

    constructor() {

        this.txt_tipodocumento = document.getElementById('txt_tipodocumento');
        this.txt_fecha = document.getElementById('txt_fecha');
        this.txt_miembro = document.getElementById('txt_miembro');
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


}