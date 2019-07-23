import { autoCompletar } from '../helper/helper.js'

export default class FormularioMiembroRequisito {    

    constructor() {

        this.idmiembro = document.getElementById('idmiembro');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.txt_idrequisito = document.getElementById('txt_idrequisito');
        this.txt_requisito = document.getElementById('txt_requisito');
        this.txt_obs = document.getElementById('txt_obs');
        this.btnAgregaItem = document.getElementById('btnAgregaItem');        

    }

    async obtenerRequisitos() {

        try {
            
            const res = await fetch('/requisitos_miembro/lista_requisitos');
            const data = await res.json();
            
            if(data)
                return data;
                
            return false;
                        
        } catch (error) {
            console.error(error.message);
        }

    }    

    async obtenerMiembros() {

        try {
            
            const res = await fetch('/requisitos_miembro/lista_personas_json');
            const data = await res.json();

            if (data)
                return data;
            
            return false;

        } catch (error) {
            console.error(error.message);
        }

    }

    async cargarInputs() {

        const personas = await this.obtenerMiembros();
        const requisitos = await this.obtenerRequisitos();
        
        autoCompletar(personas, 'persona', 'idpersona', 'idmiembro', 'txt_miembro');
        autoCompletar(requisitos, 'descripcion', 'id', 'txt_idrequisito', 'txt_requisito');

    }

    validarFormulario() {
        
        let datos = {};
        let idmiembro = this.idmiembro.value;
        let txt_miembro = this.txt_miembro.value;
        let txt_idrequisito = this.txt_idrequisito.value;
        let txt_requisito = this.txt_requisito.value;
        let txt_obs = this.txt_obs.value;

        if (idmiembro !== "" && txt_miembro !=="" && txt_idrequisito !== "" && txt_requisito !== "") {

            datos.idmiembro = idmiembro;
            datos.txt_miembro = txt_miembro.trim();
            datos.txt_idrequisito = txt_idrequisito;
            datos.txt_requisito = txt_requisito.trim();
            datos.txt_obs = txt_obs;

            return datos;

        }

        alert('Complete correctamente el formulario.');
        return false;

    }
}