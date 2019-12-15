import { mensajeConfirmacion } from '../../helper/helper.js';
/**
 * Controlador del formulario
 */

document.addEventListener('DOMContentLoaded', () => {
   // Formatear los combos con Select2
   $('select').select2();
   const alerta = `<span class="badge badge-warning">Plan futuro</span>`;
   const anho = document.getElementById('anho');
   const div = document.getElementById('alerta-anho');
   const btnEvento = document.getElementById('btAgregaEvento');
   const btnLugar = document.getElementById('btAgregaLugar');

   //Agregar eventos a los botones
   btnEvento.addEventListener('click', () => {
      const mc = mensajeConfirmacion('Confirmar', 'Desea agregar un evento ?');
      mc.buttons.Si.action = () => {
         $('#modalEvento').modal();
      }
      mc.open();
   });
   btnLugar.addEventListener('click', () => {
      const mc = mensajeConfirmacion('Confirmar', 'Desea agregar un lugar ?');
      mc.buttons.Si.action = () => {
         $('#modalLugar').modal();
      }
      mc.open();
   });

   const verificaAnho = async (anho) => {
      try {
         const res = await fetch(`/actividades/registrar_actividades_anuales/verificarAnhoFuturo/${anho}`)
         const data = await res.json();
         if (data) {
            div.innerHTML = alerta;
         }
      } catch (error) {
         console.error(error);
      }
   }

   verificaAnho(anho.value);
});