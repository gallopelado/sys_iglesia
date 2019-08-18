import { autoCompletar } from '../helper/helper.js';

export default class ModalReincorporacion {

    constructor() {

        this.idpersona = document.getElementById('idpersona');
        this.txt_persona = document.getElementById('txt_persona');                
        this.txtobs = document.getElementById('txtobs');
        this.btnProceder = document.getElementById('btnProceder');
        this.btnCancelar = document.getElementById('btnCancelar');

    }

    iniciar() {

        $('#modal_reincorporacion').modal('toggle');

    }

    async reincorporar() {

        // Obtener datos del formulario.
        const datos = {
            idmiembro: parseInt(this.idpersona.value),
            obs: this.txtobs.value.trim()
        };
        
        // Enviar al servidor.
        try {
            
            const res = await fetch('/miembro_oficial/reincorporar', {
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

}