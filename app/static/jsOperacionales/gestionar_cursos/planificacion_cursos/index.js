import { idioma_spanish } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', () => {

    sessionStorage.setItem('editar', false);

    //Cargar tabla
    var table = $('#tabla_planificacion_curso').DataTable({
        "ajax": {
            url: `/cursos/malla_curricular/mallas`
            , dataSrc: ''
        }, "columnDefs": [{
            "targets": -1,
            "data": null/*,
            "defaultContent": '<button type="button" class="btn btn-primary btn-sm ver"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Ver</button> <button type="button" class="btn btn-success btn-sm editar"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Modificar</button>'*/
        }]
        , "columns": [
            { "data": "fecharegistro" }
            , { "data": "estado" }
            , { "data": "botones" }

        ]
        , "destroy": true
        , "language": idioma_spanish
    });

     //Asignar un evento a botoncito editar. y mostrar el json asociado.
     $('#tabla_planificacion_curso tbody').on('click', '.editar', async function () {
        var data = table.row($(this).parents('tr')).data();
        //Esto muestra todo el objeto json traido de AJAX.
        //console.log(data);
        sessionStorage.setItem('anio_des', data.anho_des)
        sessionStorage.setItem('editar', true);
        sessionStorage.setItem('fecharegistro', data.fecharegistro);
        location.href = `/cursos/planificacion_cursos/form_planificacion/${data.idmalla}`;
     });

     //Asignar un evento a botoncito ver. y mostrar el json asociado.
     $('#tabla_planificacion_curso tbody').on('click', '.ver', function () {
        var data = table.row($(this).parents('tr')).data();
        //Esto muestra todo el objeto json traido de AJAX.
        sessionStorage.setItem('anio_des', data.anho_des)
        sessionStorage.setItem('editar', false);
        sessionStorage.setItem('fecharegistro', data.fecharegistro);
        location.href = `/cursos/planificacion_cursos/form_planificacion/${data.idmalla}`;
     });

});