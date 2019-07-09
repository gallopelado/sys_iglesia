import { hacerDataTable } from '../helper/helper.js';
import ModalVer from './ModalVer.js';

document.addEventListener('DOMContentLoaded', () => {
    
    hacerDataTable('tabla_formadi');
    // Activa los popovers de la tabla.
    $('[data-toggle="popover"]').popover();
    let p = new PrincipalUI();
    p.asignarModales();
});


// Función Ver
function ver(id) {
    alert("Hola");
    console.log(id);
}

/**
 * Clase PrincipalUI.
 * 
 * Se define las funcionalidades de esta primera vista.
 * 
 * @author <juanftp100@gmail.com> Juan José González
 */
class PrincipalUI {

    constructor() {
        this.tabla = document.getElementById('tabla_formadi');
    }

    mostrarMensajito(){
        // De momento el popover no funciona generando primero por javascript
        //console.log(this.tabla.rows);
        let tabla = this.tabla;

        for(let i = 1; i < tabla.rows.length; i++) {

            //console.log(tabla.rows[i]);
            
            tabla.rows[i].cells[0].onmouseenter = function () {
                // title="Header" data-toggle="popover" data-trigger="hover" data-content="Some content"
                tabla.rows[i].cells[0].dataToggle="popover";
                tabla.rows[i].cells[0].title="Holi";
                tabla.rows[i].cells[0].dataContent="Una limoznita buen hombre.";
                tabla.rows[i].cells[0].dataTrigger="hover";
                 
                console.log("Tocame, tocameeee!!");   
                console.log( tabla.rows[i].dataToggle);             
                
            }
            
        }
       
        console.log(tabla.rows);
        
    }

    asignarModales() {

        let tabla = this.tabla;

        for(let i = 1 ; i < tabla.rows.length; i++) {

            // Obtiene de la tabla > filas > celdas > hijos de esa celda > hijos de los hijos de esa celda > ligamos con evento click

            tabla.rows[i].cells[2].children[0].childNodes[1].onclick = () => {
                
                //console.log(tabla.rows[i].id);
                localStorage.setItem('idpersona', tabla.rows[i].id);
                let md = new ModalVer();
                md.mostrarModal();                
                
            }

        }

    }

}