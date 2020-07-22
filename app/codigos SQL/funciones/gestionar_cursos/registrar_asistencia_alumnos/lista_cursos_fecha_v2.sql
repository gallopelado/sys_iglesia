create or replace function cursos.lista_cursos_fecha(idmalla integer, turno turno, idprofesor integer)
returns table(malla_id integer, cur_id integer, asi_id integer, num_id integer, per_id integer, cur_des text, asi_des text, num_des text, dia text, fecha date) as
$$
declare
	malla_id integer;
	cur_id integer;
	asi_id integer;
	num_id integer;
	per_id integer;
	cur_des text;
	asi_des text;
	num_des text;
	fecha_inicio date;
	fecha_fin date;
	dias json;
	reg record;
begin
	--cargar fila 
	select v_malla_id, v_cur_id, v_asi_id, v_num_id, v_per_id, v_cur_des, v_asi_des, v_num_des, v_fecha_inicio, v_fecha_fin, v_dias 
	into   malla_id,   cur_id,   asi_id,   num_id,   per_id,   cur_des,   asi_des,   num_des,   fecha_inicio,   fecha_fin,   dias
	from cursos.obtener_dias_activos_segun_fecha(idmalla, turno, idprofesor);
	
	drop table if exists temporal_data;
	create temp table temporal_data(v_malla_id integer, v_cur_id integer, v_asi_id integer, v_num_id integer, v_per_id integer
	, v_cur_des text, v_asi_des text, v_num_des text, dia text, fecha date);
	
	for reg in SELECT * from cursos.calcula_fechas_segun_dias(fecha_inicio, fecha_fin, dias)
	loop
		insert into temporal_data 
		values(malla_id, cur_id, asi_id, num_id, per_id, cur_des, asi_des, num_des, reg.v_dia, reg.v_fecha);
	end loop;
	return query select * from temporal_data;
end
$$ language plpgsql;

select * from cursos.lista_cursos_fecha(2, 'NOCHE', 2)

select * from cursos.obtener_dias_activos_segun_fecha(2, 'NOCHE', 2)