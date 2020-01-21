document.addEventListener('DOMContentLoaded', () => {
    $('select').select2();
    window.quill = new Quill('#quill-container', {
        modules: {
            toolbar: [
                [{ header: [1, 2, false] }],
                ['bold', 'italic', 'underline'],
                ['image', 'code-block']
            ]
        },
        //scrollingContainer: '#scrolling-container',
        placeholder: 'Compose an epic...',
        theme: 'snow'  // or 'bubble'
    });
    //boton guardar
    const btnGuardar = document.getElementById('btnGuardar');
    if (btnGuardar != undefined) {
        btnGuardar.addEventListener('click', async () => {
            const idcontrato = document.getElementById('idcontrato');
            const titulo = document.getElementById('txt_titulo');
            const tipo = document.getElementById('cbo_tipo');
            const plantilla = quill.container.firstChild.innerHTML;

            //validaciones
            if (titulo.value == '') {
                alert('No debe estar vacio el titulo');
                titulo.focus();
                return false;
            }
            if (tipo.value == '') {
                alert('Debe elegir un tipo');
                tipo.focus();
                return false;
            }

            const datos = {
                idcontrato:idcontrato.value 
                , titulo: titulo.value.toUpperCase()
                , tipo: tipo.value
                , plantilla: plantilla
            }

            try {
                const res = await fetch('/contrato/guardar', {
                    method: 'POST'
                    , headers: {
                        'Content-Type': 'application/json'
                    }
                    , body: JSON.stringify(datos)
                });
                const data = await res.json()
                console.log(data);
                if (data == true) {
                    location.href = '/contrato/';
                } else {
                    location.href = '/contrato/';
                }
            } catch (error) {
                console.error(error);
            }
        });
    }    
});