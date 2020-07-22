create or replace function cursos.lista_cursos_fecha(idmalla integer, turno turno, idprofesor integer)
returns table(dia text, fecha date) as
$$
	SELECT * from cursos.calcula_fechas_segun_dias(
		(select v_fecha_inicio from cursos.obtener_dias_activos_segun_fecha(idmalla, turno, idprofesor)),
		(select v_fecha_fin from cursos.obtener_dias_activos_segun_fecha(idmalla, turno, idprofesor)),
		(select v_dias from cursos.obtener_dias_activos_segun_fecha(idmalla, turno, idprofesor))
	);
$$ language sql;

select cursos.lista_cursos_fecha(2, 'NOCHE', 2)