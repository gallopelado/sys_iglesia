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
const end_principal = '/miembro_oficial';
  // Guardar
const end_guardar = `${end_principal}/guardar`;


//Exportar todo.
export { end_principal, end_guardar};