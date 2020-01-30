create or replace function actividades.generacion_contrato(resid integer, encargadoid integer, plantillacontrato text, contratotexto text, creadoporusuario integer)
returns boolean as 
$$
/**
 * Funcion generacion_contrato
 * 
 * Inserta en la tabla contrato reserva 
 * confirmando con una actualizacion en la tabla
 * reserva.
 * 
 * Autor: Juan Jose Gonzalez Ramirez
 * Version: 1.1
 */
begin 
	if resid is null or encargadoid is null or plantillacontrato is null or plantillacontrato = '' then 
		raise exception 'Alguno de los argumentos esta vacio';
		return false;
	end if;
	--Insertar 1ero en contrato reserva
	INSERT INTO actividades.contrato_reserva
	(res_id, encargado_id, estado, plantilla_contrato, contrato_texto, creado_por_usuario, creacion_fecha)
	VALUES(resid, encargadoid, true, plantillacontrato, contratotexto, creadoporusuario, now());
	--Update a reservas
	UPDATE actividades.reservas
	SET modificado_por_usuario=creadoporusuario, modif_fecha=now(), res_estado='CONFIRMADO'
	WHERE res_id=resid;
	return true;
end
$$ language plpgsql;