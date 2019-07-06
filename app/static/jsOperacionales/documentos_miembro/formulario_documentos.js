document.addEventListener('DOMContentLoaded', () => {

    // inicio
    $('#datetimepicker4').datetimepicker({
        format: 'L',
        locale: 'es',
        format: 'DD/MM/YYYY',
        maxDate: new Date()
    });

    let doc = new FormularioDocumentos();
    doc.cargarTiposDocumentos();
    doc.cargarPersonas();


});