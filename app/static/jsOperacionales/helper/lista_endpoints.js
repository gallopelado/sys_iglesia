/**
 * Descripcion: El propósito de este fichero es reunir los endpoints por modulo,
 * es decir, todas aquellas rutas que usamos con AJAX.
 * @author: Juan José González Ramírez
 * @email: juanftp100@gmail.com
 */

 /**
  * Modulo: Gestionar Membresía
  */

  // 05. Registrar Formulario De Miembro Oficial
  // Vista principal
const end_principal_miembrooficial = '/miembro_oficial';
  // Guardar
const end_guardar_miembrooficial = `${end_principal_miembrooficial}/guardar`;
const end_modificar_miembrooficial = `${end_principal_miembrooficial}/modificar`;
const end_carga_modificar = `${end_principal_miembrooficial}/frm_miembro`;
const end_baja_miembrooficial = `${end_principal_miembrooficial}/baja`;


//Exportar todo.
export { end_principal_miembrooficial, end_guardar_miembrooficial, end_carga_modificar, end_modificar_miembrooficial, end_baja_miembrooficial};