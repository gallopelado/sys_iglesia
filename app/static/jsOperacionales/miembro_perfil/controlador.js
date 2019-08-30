    

    function validarForm(formu) {
        
        //const formu = document.forms['formulario_perfil'];
        
        // Validar cualidades personales.
        const cualidades = formu.txt_cualipers;
        if (cualidades.value.trim() == '') {
            
            alert('Debe proporcionar las cualidades');
            cualidades.focus();
            cualidades.select();            
            return false;

        } 

        // Validamos actitudes ministeriales.
        const actitudes = formu.txt_actiminis;
        if (actitudes.value.trim() == '') {

            alert('Debe proporcionar las actitudes ministeriales');   
            actitudes.focus();
            actitudes.select();         
            return false;

        }

        // Validamos si seleccionó al algún ministerio.
        const ministerios = formu.ministerios;
        
        let miniSeleccionado = false;

        // Revisamos si se selecciono
        for (let i = 0; i < ministerios.length; i++) {

            if (ministerios[i].selected) {
                
                miniSeleccionado = true;

            }

        }

        if (!miniSeleccionado) {

            alert('Debe escojer algún ministerio');
            return false;

        }

        // Formulario correcto, enviar !
        alert('Formulario válido, enviando datos');
        return true;
        

    }




