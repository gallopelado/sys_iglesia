import { end_principal_miembrooficial } from '../helper/lista_endpoints.js';
export default class ModalBaja {

    /**
     * Metodo constructor de la clase ModalBaja.
     * 
     * Se recopila los objetos y sus propiedades de dicho elemento.
     * 
     */
    constructor() {
        this.idpersona = document.getElementById('idadmision'),
            this.txt_persona = document.getElementById('txt_persona'),
            this.chk_disciplina = document.getElementById('chk_disciplina'),
            this.chk_defuncion = document.getElementById('chk_defuncion'),
            this.chk_excomunion = document.getElementById('chk_excomunion'),
            this.chk_traslado = document.getElementById('chk_traslado'),
            this.chk_otras = document.getElementById('chk_otras'),
            this.txtobs = document.getElementById('txtobs');
    }

    /**
     * Metodo obtenerDatos.
     * 
     * Obtiene registros en formato JSON segun el idadmision enviado.(ASINCRONA)
     * 
     * @param {*} id 
     * @returns {json} datos
     */
    async obtenerDatos(id) {

        let data = {
            idadmision: id
        }

        try {

            const res = await fetch('http://localhost:5000/formulario_admision/obtener_datos_modal', {
                method: 'POST',
                headers: {
                    'Accept': 'applications/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const datos = await res.json()

            return datos;

        } catch (error) {

            console.error(error);
            return false;
        }

    }

    /**
     * Metodo eliminar.
     * 
     * Envia datos tipo json al controlador.(ASINCRONA)
     * 
     */
    async eliminar() {

        let datos = this.obtenerDatosFormulario();

        try {

            const res = await fetch('http://localhost:5000/formulario_admision/dar_de_baja', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });

            const data = await res.json();
            if (data.cambiado === true) {

                $('#modal_baja').modal('toggle');
                
                // Redireccionar a la pagina.
                location.href = end_principal_miembrooficial;


            } else {
                console.error(data);
            }

            console.log(data);

        } catch (error) {
            console.error(error);
        }

    }

    obtenerDatosFormulario() {

        let datos, radioElegido, radios = [
            "chk_disciplina",
            "chk_defuncion",
            "chk_excomunion",
            "chk_traslado",
            "chk_otras"
        ];

        // Recorrer el array en busca del elemento elegido.
        for (let i = 0; i < radios.length; i++) {

            if (document.getElementById(radios[i]).checked === true) {

                radioElegido = radios[i];

                switch (radioElegido) {

                    case "chk_disciplina":

                        radioElegido = "DISCIPLINA";
                        break;

                    case "chk_defuncion":

                        radioElegido = "DEFUNCION";
                        break;

                    case "chk_excomunion":

                        radioElegido = "EXCOMUNION";
                        break;

                    case "chk_traslado":

                        radioElegido = "TRASLADO";
                        break;

                    case "chk_otras":

                        radioElegido = "OTRAS";
                        break;

                }

            }

        }

        // Preparar el objeto json.
        datos = {
            idadmision: this.idpersona.value,
            razonbaja: radioElegido,
            obs: this.txtobs.value.trim() !== '' ? this.txtobs.value : null
        }

        return datos;
    }

}
