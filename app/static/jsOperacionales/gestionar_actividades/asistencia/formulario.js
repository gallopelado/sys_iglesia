document.addEventListener('DOMContentLoaded', () => {

    $('select').select2();
    const btGuardar = document.getElementById('btnGuardar');
    btGuardar.addEventListener('click', async() => {

        const idasistencia = document.getElementById('idasistencia');
        const txt_fecha = document.getElementById('txt_fecha');
        const cbo_evento =  document.getElementById('cbo_evento');
        const txt_obs = document.getElementById('txt_obs');
        const tbody =  document.getElementById('tbody');        
        const size = tbody.rows.length;
        let cadena_persona = '';
        let cadena_asistio = '';
        let cadena_puntual = '';
        let datos = {};
        if ( size == undefined || size <= 0 ) {
            alert('No hay elementos en la tabla');
            return false;
        }
        if ( cbo_evento.value == '' ) {
            alert('Debe seleccionar un evento');
            cbo_evento.focus();
            return false;
        }
        if ( txt_obs.value == '' ) {
            alert('Debe escribir una descripcion');
            txt_obs.focus();
            return false;
        }

        // el primer children es para el check 1 de asistio, el 2 es para puntualidad
        // tbody.rows[0].children[1].children[0].children[0].checked
        // tbody.rows[0].children[2].children[0].children[0].checked
        for ( let i = 0; i <= size-1; i++ ) {

            //Acumular los idpersona, asistio y puntualidad
            let idpersona =tbody.rows[i].id;
            cadena_persona += `${idpersona},`;
            cadena_asistio += `${tbody.rows[i].children[1].children[0].children[0].checked},`;
            cadena_puntual += `${tbody.rows[i].children[1].children[0].children[0].checked==true ? tbody.rows[i].children[2].children[0].children[0].checked : false},`;
        }
         // Limpieza de la última coma.
         cadena_persona = cadena_persona.slice(0, (cadena_persona.length - 1));
         cadena_asistio = cadena_asistio.slice(0, (cadena_asistio.length - 1));
         cadena_puntual = cadena_puntual.slice(0, (cadena_puntual.length - 1));

         datos = {
            idasistencia:idasistencia.value
            , txt_fecha:txt_fecha.value
            , cbo_evento:cbo_evento.value
            , txt_obs:txt_obs.value.trim()
            , opcion:idasistencia.value==''?'registrar':'modificar'
            , cadena_persona:cadena_persona
            , cadena_asistio:cadena_asistio
            , cadena_puntual:cadena_puntual
         }
         try {
             const res = await fetch('/actividades/registrar_asistencia/guardar', {
                 method:'POST'
                 , headers:{
                     'Content-Type':'application/json'
                 }
                 ,body:JSON.stringify(datos)
             });
             const data = await res.json();
             console.log(data);
             if ( data.estado == true ) {
                 alert('Se procesó correctamente su acción');   
                 location.href = '/actividades/registrar_asistencia/';
             } else  {
                 console.error(res);
             }
         } catch (error) {
             console.error(error);
         }
    });      

});