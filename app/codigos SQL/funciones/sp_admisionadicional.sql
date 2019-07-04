-----------------------------------------------------------------------------
--
-- Crear una funcion que guarde los datos del formulario de datos adicionales.
--
-----------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION sp_formulario_adicional(idpersona integer, idnacionalidad integer, 
lugarnacimiento varchar, alergias varchar, tiposangre integer, capacidad_diferente varchar, v_datos_tabla_nuevos text[], v_datos_tabla_eliminar text[])
returns void as
$$
/**
 * Procedimiento: sp_formulario_adicional
 * Autor: Juan José González Ramírez
 * Fecha creación: 2019-06-29
 * Parametros: idpersona integer, idnacionalidad integer, lugarnacimiento varchar, 
 * alergias varchar, tiposangre integer, capacidad_diferente varchar
 * Descripción: Procedimiento que cargará en las tablas admision_adicionales, historial_profesiones.
 * 
 */
declare
	
	-- Define la estructura temporal que servirá para realizar las operaciones.
	temp_row membresia.admision_adicionales%rowtype;	

begin
	
	-- Capturar datos del formulario.
	temp_row.add_id := idpersona;
	temp_row.nac_id := idnacionalidad;
	temp_row.add_lugarnac := UPPER(TRIM(lugarnacimiento));
	temp_row.san_id := tiposangre;
	temp_row.add_alergias := UPPER(TRIM(alergias));
	temp_row.add_capacdife := UPPER(TRIM(capacidad_diferente));
	
	-- Capturar el usuario.
	temp_row.creado_por_usuario := null;	
	
	-- Bloque de la matriz.
	declare
	
		coleccion text[];
	
	begin
		
		coleccion := v_datos_tabla_nuevos;
		
		-- Se verifica si la matriz no esta vacia
		 if array_length(coleccion, 1) > 0 then
		 	raise notice 'La matriz contiene datos %', coleccion;
		 else
		 	raise exception 'La matriz esta vacía';
		 end if;
	end;
end;
$$ language plpgsql;


--SELECT add_id, nac_id, add_lugarnac, san_id, add_alergias, add_capacdife, add_foto, fecha_creado, add_estado, creado_por_usuario FROM membresia.admision_adicionales;



