
import FormularioDocumentos from './Clase_FormularioDocumentos.js';

document.addEventListener('DOMContentLoaded', () => {

    // inicio
    $('#datetimepicker4').datetimepicker({
        format: 'L',
        locale: 'es',
        format: 'DD/MM/YYYY',
        maxDate: new Date()
    });

    const doc = new FormularioDocumentos();
    doc.cargarTiposDocumentos();
    doc.cargarPersonas();

    // Eventos a botones.
    const btGuardar = doc.btnGuardar;
    const documento = doc.txt_documento;
    documento.addEventListener('change', mostrarNombre);
    btGuardar.addEventListener('click', guardar);

    // Cargar el formulario.
    doc.cargarFormulario();

});

function guardar() {

    const doc = new FormularioDocumentos();
    doc.guardarFormulario();

}

function mostrarNombre() {

    const doc = new FormularioDocumentos();
    // Captura del objeto file.
    const documento = doc.txt_documento;
    const div = document.getElementById('txt_nombredocumento');
    const fichero = documento.files[0];

    div.innerHTML = `
    
        <div class="card-header bg-secondary">
                    <strong class="card-title text-light">Nombre del documento</strong>
        </div>
        <div class="card-body text-white bg-primary">
            <p class="card-text text-light">${fichero.name}</p>
        </div>

    `

}