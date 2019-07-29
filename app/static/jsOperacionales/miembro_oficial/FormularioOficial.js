import { autoCompletar } from '../helper/helper.js';

export default class FormularioOficial {

    constructor() {

        this.txt_idmiembro = document.getElementById('txt_idmiembro');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.txt_razonalta = document.getElementById('txt_razonalta');
        this.txt_fechaconversion = document.getElementById('txt_fechaconversion');
        this.txt_fechabautismo = document.getElementById('txt_fechabautismo');
        this.txt_estadomembresia = document.getElementById('txt_estadomembresia');
        this.txt_lugarbautismo = document.getElementById('txt_lugarbautismo');
        this.txt_ministro = document.getElementById('txt_ministro');
        this.txt_fechainiciomembresia = document.getElementById('txt_fechainiciomembresia');
        this.chk_fuebautizado = document.getElementById('chk_fuebautizado');
        this.chk_padreseniglesia = document.getElementById('chk_padreseniglesia');
        this.chk_recibioes = document.getElementById('chk_recibioes');
        this.txt_obs = document.getElementById('txt_obs');
        this.btnGuardar = document.getElementById('btnGuardar');
        this.btnCancelar = document.getElementById('btnCancelar');
    }

    async autocompletarMiembro() {

        const endpoint = '/miembro_oficial/personas_activas';

        try {
            
            const res = await fetch(endpoint);
            const data = await res.json();
            //console.log(data);
            const idmiembro = this.txt_idmiembro.id;
            const miembro = this.txt_miembro.id;
            autoCompletar(data, 'persona', 'idadmision', idmiembro, miembro);

        } catch (error) {
            console.error(error);
        }
        
    }

}