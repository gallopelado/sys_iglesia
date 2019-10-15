export default class ModalVer {

    constructor() {
        this.txt_ministerio = document.getElementById('txt_ministerio');
        this.txt_cualipers = document.getElementById('txt_cualipers');
        this.txt_actimin = document.getElementById('txt_actimin');
        this.txt_antecedentes = document.getElementById('txt_antecedentes');
        this.txt_ultimafecha = document.getElementById('txt_ultimafecha');
    }

    async getPerfil(idperfil) {

        try {
            
            const res = await fetch(`/membresia/registrar_calificados/traer_perfil_id/${idperfil}`);
            const data = await res.json();            

            //Limpiar campos

            this.txt_ministerio.value = '';
            this.txt_cualipers.value = '';
            this.txt_actimin.value = '';
            this.txt_antecedentes.value = '';
            this.txt_ultimafecha.innerHTML = '';

            this.txt_ministerio.value = data.serviren;
            this.txt_cualipers.value = data.cualidad_personal;
            this.txt_actimin.value = data.actitud_ministerial;
            this.txt_antecedentes.value = data.antecendentes;
            this.txt_ultimafecha.innerHTML = data.ultimafecha;

        } catch (error) {
            console.error(error);
        }

    }

}