create or replace function actividades.gestionar_asistencia(
	opcion varchar
	, asisid integer
	, eveid integer
	, asisdes varchar
	, lista_personas varchar
	, lista_asistio varchar
	, lista_puntual varchar
) returns boolean as $$
/**
 * Procedimiento gestionar_asistencia
 * Se define el CRUD para las actividades anuales
 * con opciones como:
 * registrar, modificar, baja
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * versión 1.0
*/
declare
	v_asisid integer;
	v_lista_personas varchar := trim(lista_personas);
	v_lista_asistio varchar := trim(lista_asistio);
	v_lista_puntual varchar := trim(lista_puntual);
	v_asisdes varchar := trim(upper(asisdes));
	size_personas integer;
	size_asistio integer;
	size_puntual integer;
	array_personas varchar[];
	array_asistio varchar[];
	array_puntual varchar[];
	fecha_actual TIMESTAMP := now();
	v_idpersona integer;
	v_asistio boolean;
	v_puntual boolean;
begin
	--limpieza
	if v_lista_personas is null or v_lista_personas = '' then
		raise exception 'No se ha recibido ninguna persona';
		return false;
	end if;
	if v_lista_asistio is null or v_lista_asistio = '' then
		raise exception 'No se ha recibido ninguna asistencia';
		return false;
	end if;
	if v_lista_puntual is null or v_lista_puntual = '' then
		raise exception 'No se ha recibido ninguna puntualidad';
		return false;
	end if;

	--Cargar los arrays
	array_personas := string_to_array(v_lista_personas, ',');
	array_asistio := string_to_array(v_lista_asistio, ',');
	array_puntual := string_to_array(v_lista_puntual, ',');

	--Obtener el tamaño
	size_personas := array_upper(array_personas, 1);
	size_asistio := array_upper(array_personas, 1);
	size_puntual := array_upper(array_personas, 1);

	--Validar tamaños
	if size_personas != size_asistio or size_personas != size_puntual then
		raise exception 'No se ha recibido correctamente las personas o asistencias o puntualidades';
		return false;
	end if;

	case opcion
		when 'registrar' then
			--Insertar la cabecera
			INSERT INTO actividades.cabe_asistencia
			(asis_des, asis_estado, creado_por_usuario, creacion_fecha, modificado_por_usuario, modif_fecha)
			VALUES(v_asisdes, true, null, fecha_actual, null, null) returning asis_id into v_asisid;
			raise notice 'Se insertó correctamente la cabecera = %',asis_id;
			--Ahora cargar los arrays
			for i in 1..array_personas
			loop
				--Colectar de a uno
				v_idpersona := array_personas[i]::int;
				v_asistio := array_asistio[i];
				v_puntual := array_puntual[i];
				--Insertar el detalle
				INSERT INTO actividades.det_asistencia
				(asis_id, per_id, asistio, puntual)
				VALUES(v_asisid, v_idpersona, v_asistio, v_puntual);				
			end loop;
			return true;

		when 'modificar' then
			--Actualizar la cabecera
			UPDATE actividades.cabe_asistencia
			SET eve_id = eveid, asis_des = asisdes, 
			modificado_por_usuario = null, modif_fecha = fecha_actual
			WHERE asis_id = asisid;
		
			for i in 1..array_personas
			loop
				--Colectar de a uno
				v_idpersona := array_personas[i]::int;
				v_asistio := array_asistio[i];
				v_puntual := array_puntual[i];
				--Actualizar el detalle
				UPDATE actividades.det_asistencia
				SET asistio = v_asistio, puntual = v_puntual
				WHERE asis_id = asisid AND per_id = v_idpersona;				
			end loop;
			return true;

		when 'baja' then
			--Actualizar la cabecera
			UPDATE actividades.cabe_asistencia
			SET asis_estado = false, 
			modificado_por_usuario = null, modif_fecha = fecha_actual
			WHERE asis_id = asisid;
			return true;
		else 
			raise exception 'Ninguna opción ingresada es la correcta';
			return false;
		end case;
end 
$$ language plpgsql;

