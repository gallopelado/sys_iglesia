/**
 * Clase ModalVer.
 * 
 * Se definen los métodos para manipular
 * el modalVer de la vista principal.
 * 
 * @author <juanftp100@gmail.com> Juan José González Ramírez
 */
class ModalVer {

    constructor() {

        this.modal = $("#modalVer");
        this.txt_persona = document.getElementById('txt_persona');
        this.txt_nacionalidad = document.getElementById('txt_nacionalidad');
        this.txt_lugarnac = document.getElementById('txt_lugarnac');
        this.txt_alergia = document.getElementById('txt_alergia');
        this.txt_sangre = document.getElementById('txt_sangre');
        this.txt_capacidades = document.getElementById('txt_capacidades');
        this.foto = document.getElementById('img_foto');
        this.tbody_tabla = document.getElementById('tbody_profesiones');
    }

    mostrarModal() {

        this.modal.modal();
        this.setearFormulario();

    }

    async obtenerDatos() {

        let datos = {
            idadi: localStorage.getItem('idpersona')
        }

        try {

            const res = await fetch('obtener_frmdatos_id_json', {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            return data;

        } catch (error) {

            console.error(error);

        }


    }

    async obtenerDatosTabla() {

        let datos = {
            idadi: localStorage.getItem('idpersona')
        }

        try {

            const res = await fetch('obtener_historial_profesiones', {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            return data;

        } catch (error) {

            console.error(error);

        }


    }


    async setearFormulario() {

        let data = await this.obtenerDatos(), tablaContent = await this.obtenerDatosTabla(), cadena = "";

        //console.log(tablaContent[0]);

        const d = data[0][0];

        this.txt_persona.value = d.persona;
        this.txt_nacionalidad.value = d.nacionalidad;
        this.txt_lugarnac.value = d.lugarnacimiento;
        this.txt_alergia.innerHTML = d.alergias;
        this.txt_sangre.value = d.sangre;
        this.txt_capacidades.innerHTML = d.capacidades;
        this.foto.src = `http://localhost:5000/static/multimedia/membresia/02_adicionales/imagenes/${d.foto}`;

        this.tbody_tabla.innerHTML = "";

        // Setear la tabla
        if (tablaContent[0]) {

            tablaContent[0].forEach(item => {

                cadena += `
                <tr>                    
                    <td>${item.profesion}</td>
                    <td>${item.puesto_laboral}</td>
                    <td>${item.lugar_trabajo}</td>
                </tr>
            `;

            });
            this.tbody_tabla.innerHTML = cadena;
        } else {
            this.tbody_tabla.innerHTML = "No hay elementos registrados...";
        }

       
    }
}