/**
 * Clase ModalVer.
 * 
 * Se definen los métodos para manipular
 * el modalVer de la vista principal.
 * 
 * @author <juanftp100@gmail.com> Juan José González Ramírez
 */
export default class ModalVer {

    constructor() {

        this.modal = $("#modalVer");
        this.txt_tipodocumento = document.getElementById('txt_tipodocumento');
        this.txt_fecha = document.getElementById('txt_fecha');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.txt_conyuge = document.getElementById('txt_conyuge');
        this.txt_oficiador = document.getElementById('txt_oficiador');
        this.txt_declaracion = document.getElementById('txt_declaracion');
        this.txt_notas = document.getElementById('txt_notas');
        this.txt_testigo1 = document.getElementById('txt_testigo1');
        this.txt_testigo2 = document.getElementById('txt_testigo2');

    }

    mostrarModal() {

        this.modal.modal();        

    }

    async obtenerDatos(idmiembro, idtipodocumento) {

        const datos = {
            idmiembro: idmiembro,
            idtipodocumento: idtipodocumento
        }

        try {

            const res = await fetch('obtener_miembro_documento', {
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

    


    async setearFormulario(idmiembro, idtipodocumento) {

        let data = await this.obtenerDatos(idmiembro, idtipodocumento);

        console.log(data);
       
        this.txt_tipodocumento.value = data.documento;
        this.txt_fecha.value = data.fechadocumento;
        this.txt_miembro.value = data.persona;
        this.txt_conyuge.value = data.conyuge;
        this.txt_oficiador.value = data.oficiador;
        this.txt_declaracion.value = data.declaracion;
        this.txt_notas.value = data.notas;
        this.txt_testigo1.value = data.testigo1;
        this.txt_testigo2.value = data.testigo2;
    }
}