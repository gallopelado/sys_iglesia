class ModalProfesion {


    constructor() {

        this.descripcion = document.getElementById('txt_descripcion');
        this.btnguardar = document.getElementById('btnGuardarProfesion');
        this.formulario;
        /*this.btnguardar.addEventListener('click',() => {
            this.guardar();
        });*/

    }

    mostrar() {

        $('#modalprofesion').modal();

    }

    cerrar() {

        $('#modalprofesion').modal('toggle');

    }

    obtenerDatosForm() {

        let descripcion = this.descripcion.value.trim();
        if (descripcion !== "") {

            this.formulario = new FormData();
            this.formulario.append('op', 'a');
            this.formulario.append('descripcion', descripcion);

            return this.formulario;

        } else {
            return false;
        }

    }

    async guardar() {

        try {

            let datos = this.obtenerDatosForm();

            if (datos) {

                const res = await fetch('http://localhost:5000/profesion/guardar', {
                    method: 'POST',
                    body: datos
                });

                const data = res.json();

                console.log(data);

            }

        } catch (error) {
            console.error(error);
            return false;
        }


    }

}