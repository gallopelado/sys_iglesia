document.addEventListener('DOMContentLoaded', () => {

    window.modificar = (idcomite) => {
        const conf = confirm('Desea modificarlo?');
        if (conf) {
            location.href = `/membresia/registrar_comite/formulario/${idcomite}`;
        }
    }

    window.baja = (idcomite) => {
        const conf = confirm('Desea dar de baja?');
        if (conf) {
            // Iniciar modal.
            $('#modal_baja').modal();
            const btProceder = document.getElementById('btnProceder');
            btProceder.addEventListener('click', () => {                
                const obs = document.getElementById('txtobs');
                const id = idcomite;
                if (obs.value.trim() === '') {
                    alert('No puede estar sin descripción !');
                    obs.focus();                    
                } else {
                    //Enviar datos al servidor
                    let txtobs = obs.value.trim();
                    txtobs = txtobs.replace(/\\n/g, '');
                    darBaja(id, txtobs);
                }
            });
        }
    }

    const darBaja = async(id, obs) => {
        try {
            const res = await fetch('/membresia/registrar_comite/dar_baja', {
                method: 'PUT'
                , headers: {
                    'Content-Type': 'application/json'
                }
                , body: JSON.stringify({obs:obs, id: id})
            });
            const data = await res.json();
            if (data.estado === true) {
                document.getElementById('txtobs').value = '';
                $('#modal_baja').modal('toggle');
                location.href = '/membresia/registrar_comite/';
            } else {
                console.error(data);
                alert('Hubo un error, contacte con el Administrador del Sistema');
            }   
        } catch (error) {                        
            console.error(error);
            alert('Hubo un error, contacte con el Administrador del Sistema');
        }
    }

    window.reactivar = (idcomite) => {
        const conf = confirm('Desea reactivar este comité ?');
        if (conf) {
            location.href = `/membresia/registrar_comite/reactivar_comite/${idcomite}`;
        }
    }


});