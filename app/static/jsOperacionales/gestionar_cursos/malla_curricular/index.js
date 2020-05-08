import { idioma_spanish } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {

    //Cargar tabla
    var table = $('#tabla_malla_curricular').DataTable({
        "ajax": {
            url: `/cursos/malla_curricular/mallas`
            , dataSrc: ''
        }, "columnDefs": [{
            "targets": -1,
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-primary btn-sm ver"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Ver</button> <button type="button" class="btn btn-success btn-sm editar"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Modificar</button>'
        }]
        , "columns": [
            { "data": "fecharegistro" }
            , { "data": "estado" }
            , { "data": "" }

        ]
        , "destroy": true
        , "language": idioma_spanish
    });


});