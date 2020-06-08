import { idioma_spanish } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {

    sessionStorage.setItem('editar', false);

    //Cargar tabla
    var table = $('#tabla_curso').DataTable({
        "ajax": {
            url: `/cursos/inscripcion_alumnos/get_cursos_planificados`
            , dataSrc: ''
        }, "columnDefs": [{
            "targets": -1,
            "data": null/*,
            "defaultContent": '<button type="button" class="btn btn-primary btn-sm ver"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Ver</button> <button type="button" class="btn btn-success btn-sm editar"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Modificar</button>'*/
        }]
        , "columns": [
            { "data": "curso" }
            , { "data": "btn_inscribir" }

        ]
        , "destroy": true
        , "language": idioma_spanish
    });

     //Asignar un evento a botoncito editar. y mostrar el json asociado.
     $('#tabla_curso tbody').on('click', '.inscribir', async function () {
        var data = table.row($(this).parents('tr')).data();
        //Esto muestra todo el objeto json traido de AJAX.
        console.log(data);
        sessionStorage.setItem('pre_data', JSON.stringify(data))              
        location.href = `/cursos/inscripcion_alumnos/form_inscripcion`;
     });

});