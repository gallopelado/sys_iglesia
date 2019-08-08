import { autoCompletar, dateTimePicker4, mensajeConfirmacion, mensajeNormal } from '../helper/helper.js';
import { end_guardar, end_principal } from '../helper/lista_endpoints.js';

export default class FormularioOficial {

    constructor() {

        this.txt_idmiembro = document.getElementById('txt_idmiembro');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.txt_idrazonalta = document.getElementById('txt_idrazonalta');
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
        this.btnFormAdmi = document.getElementById('btnFormAdmi');
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

    async autoCompletarRequisitos() {

        const endpoint = '/requisito/lista_requisito';
        const res = await fetch(endpoint);
        const data = await res.json();

        const idrazon = this.txt_idrazonalta.id;
        const razon = this.txt_razonalta.id;
        autoCompletar(data, 'descripcion', 'id', idrazon, razon);

    }

    /**
     * Funcion formatearFechas.
     * 
     * Activa el calendario muy vistoso en los campos.
     * 
     */
    formatearFechas() {

        dateTimePicker4('picker_fechaconversion');
        dateTimePicker4('picker_fechabautismo');
        dateTimePicker4('picker_fechainiciomembresia');

    }

    /**
     * Método abrirFormularioAdmision.
     * 
     * Luego del mensaje de confirmación, se redirige al
     * formulario de admisión.
     */
    abrirFormularioAdmision() {

        const conf = mensajeConfirmacion('Mensaje de confirmación', 'Desea realizar una nueva admisión ?');
        conf.buttons.Si.action = () => {
            open('/formulario_admision/frm_admi');
        };
        // Dibujar mensaje.
        conf.open();


    }

    validarFormulario() {

        const identificadores = [
            'txt_idmiembro', 'txt_miembro', 'txt_idrazonalta', 'txt_razonalta',
            'txt_fechaconversion', 'txt_fechabautismo', 'txt_estadomembresia',
            'txt_lugarbautismo', 'txt_ministro', 'txt_fechainiciomembresia'
        ];
        const longi = identificadores.length;

        for (let i = 0; i < longi; i++) {

            if (document.getElementById(identificadores[i]).value === '') {

                const msg = mensajeNormal('Cuidado!', `Algún campo parece no estar correctamente completado. Los campos obligatorios tienen un (*)`);
                msg.open();

                return false;

            }

        }

        return true;

    }

    recuperaDatosForm() {

        const validar = this.validarFormulario();

        if (validar) {

            const datosForm = {
                idmiembro: parseInt(this.txt_idmiembro.value),
                idrazonalta: parseInt(this.txt_idrazonalta.value),
                fechaconversion: this.txt_fechaconversion.value,
                fechabautismo: this.txt_fechabautismo.value,
                estadomembresia: this.txt_estadomembresia.value,
                lugarbautismo: this.txt_lugarbautismo.value.trim() !== '' ? this.txt_lugarbautismo.value.toUpperCase() : null,
                ministro: this.txt_ministro.value.trim() !== '' ? this.txt_ministro.value.toUpperCase() : null,
                fechainiciomembresia: this.txt_fechainiciomembresia.value,
                fuebautizado: this.chk_fuebautizado.checked,
                padreseniglesia: this.chk_padreseniglesia.checked,
                recibioes: this.chk_recibioes.checked,
                observacion: this.txt_obs.value.trim() !== '' ? this.txt_obs.value.toUpperCase() : null
            }

            return datosForm;

        }

        return false;

    }

    async guardar() {

        const formulario = this.recuperaDatosForm();
        console.log(formulario);
        if (formulario) {

            try {

                const res = await fetch(end_guardar, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/ json'
                    },
                    body: JSON.stringify(formulario)
                });
                const data = await res.json();

                if (data.guardado === true) {

                    const m = mensajeNormal('Exito!', 'Se ha guardado correctamente');
                    m.open();
                    setTimeout(() => {
                        location.href = end_principal;
                    }, 3000
                    )
                    return true;

                } else {

                    const m = mensajeNormal('Upps!', 'Aparentemente se ha detectado un problema al guardar, podria ser que el registro ya existe o el miembro no cumple con los requisitos');
                    m.open();
                    return false;

                }

            } catch (error) {
                console.error(error);
            }

        }

    }
}