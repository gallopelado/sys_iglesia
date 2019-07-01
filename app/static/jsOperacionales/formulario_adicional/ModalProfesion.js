class ModalProfesion {


    constructor() {

        this.descripcion = document.getElementById('txt_descripcion');
        this.btnguardar = document.getElementById('btnGuardarProfesion');
        this.formulario;
        // Se asigna el evento click al boton.
        this.btnguardar.addEventListener('click', () => {
            // Se llama al metodo guardar.
            this.guardar();

        });

    }

    mostrar() {

        this.descripcion.focus();
        this.descripcion.className = 'input-sm form-control-sm form-control';
        $('#modalprofesion').modal();

    }

    cerrar() {

        $('#modalprofesion').modal('toggle');

    }

    obtenerDatosForm() {

        // Se recupera y limpia de espacios en blanco a los costados. Fundamental.
        let descripcion = this.descripcion.value.trim();
        if (descripcion !== "") {

            this.formulario = new FormData();
            this.formulario.append('op', 'a');
            this.formulario.append('descripcion', descripcion.toUpperCase());

            return this.formulario;

        } else {
            this.descripcion.focus();
            this.descripcion.className = 'input-sm is-invalid form-control form-control-sm';
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

                const data = await res.json();

                if(data.guardado === true) {

                    // Se limpia el campo descripcion.
                    this.descripcion.value = '';
                    // Se cierra el modal.
                    this.cerrar();
                    // Se crea la instancia del mensaje de confirmacion.
                    let v = mensajeNormal('Éxito', 'Se agregó el registro');                                        
                    // Se refresca el combo profesion.
                    let adi = new FormAdicionalUI();
                    adi.refrescarComboProfesion();
                    // Se muestra el mensaje.
                    v.open();

                } else {
                    console.error(data.guardado);
                }

            } else {

                console.error('Error al validar formulario de profesión');
            }

        } catch (error) {
            console.error(error);
            return false;
        }


    }

}