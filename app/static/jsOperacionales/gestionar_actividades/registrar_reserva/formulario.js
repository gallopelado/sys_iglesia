import { mensajeConfirmacion,mensajeNormal } from '../../helper/helper.js';
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
   const btGuardarEvento = document.getElementById('btnevento');
   const btGuardarLugar = document.getElementById('btnlugar');
   const txt_evento = document.getElementById('txt_evento');
   const txt_lugar = document.getElementById('txt_lugar');

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

   btGuardarEvento.addEventListener('click', async() => {
      let evento = txt_evento.value;
      if(evento.trim() == '') {
         alert('No puede estar vacia la descripcion');
         txt_evento.focus();
         return false;
      }
      //Guardar y cerrar modal.
      evento = evento.trim();
      evento = evento.toUpperCase();
      evento = evento.replace(/(\r\n|\n|\r)/gm,"")
      const res = await nuevoRegistro('referenciales','eventos',evento);
      if (res == true) {
         $('#modalEvento').modal('toggle');
         //Mostrar mensaje de registrado
         const m = mensajeNormal('Aviso', 'Se ha agregado un nuevo registro, se actualizara la pagina');
         m.open();
         setTimeout(() => {
            location.reload();
         }, 2000);
      }
   });
   btGuardarLugar.addEventListener('click', async() => {
      let lugar = txt_lugar.value;
      if(lugar.trim() == '') {
         alert('No puede estar vacia la descripcion');
         txt_lugar.focus();
         return false;
      }
      //Guardar y cerrar modal.
      lugar = lugar.trim();
      lugar = lugar.toUpperCase();
      lugar = lugar.replace(/(\r\n|\n|\r)/gm,"")
      const res = await nuevoRegistro('referenciales','lugares',lugar);
      if (res == true) {
         $('#modalLugar').modal('toggle');
         //Mostrar mensaje de registrado
         const m = mensajeNormal('Aviso', 'Se ha agregado un nuevo registro, se actualizara la pagina');
         m.open();
         setTimeout(() => {
            location.reload();
         }, 2000);
      }
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

   const nuevoRegistro = async(esquema,tabla,valor) => {
      try {
         const res = await fetch(`/referencial_simple/nuevo_registro`, {
            method:'POST'
            , headers:{
               'Content-Type':'application/json'
            }
            , body:JSON.stringify({esquema:esquema,tabla:tabla,valor:valor})
         })
         const data = await res.json();
         return data.procesado;
      } catch (error) {
         console.error(error);
      }
   }

   verificaAnho(anho.value);
});