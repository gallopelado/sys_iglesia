--tabla visi_hospi
create table actividades.visi_hospi(
	vh_id serial primary key
	, solicitante_id integer not null
	, paciente_id integer not null
	, idi_id integer not null
	, vh_des text not null
	, vh_esmiembro boolean not null default false
	, vh_estaenterado boolean not null default false 
	, vh_nombrehospi varchar(150) not null 
	, vh_nrocuarto varchar(10) not null 
	, vh_nrotelcuarto varchar(60)
	, vh_fechaadmi date
	, vh_diagnostico text
	, vh_direhospi varchar(100) not null
	, vh_horavisi time not null
	, vh_lunes boolean not null default false
	, vh_martes boolean not null default false
	, vh_miercoles boolean not null default false
	, vh_jueves boolean not null default false
	, vh_viernes boolean not null default false
	, vh_sabado boolean not null default false
	, vh_domingo boolean not null default false
	, foreign key(solicitante_id)references membresia.admision_persona(adp_id)
	on delete restrict on update cascade
	, foreign key(paciente_id)references referenciales.personas(per_id)
	on delete restrict on update cascade
	, foreign key(idi_id)references referenciales.idiomas(idi_id)
	on delete restrict on update cascade
);

alter table actividades.visi_hospi add column creado_por_usuario integer;
alter table actividades.visi_hospi add column creacion_fecha timestamp not null;
alter table actividades.visi_hospi add column modificado_por_usuario integer;
alter table actividades.visi_hospi add column modif_fecha timestamp;
alter table actividades.visi_hospi add column vh_estado boolean not null default true;

alter table actividades.visi_hospi drop column vh_estado;
alter table actividades.visi_hospi add column vh_estado estado_solicitud_hospital;
update actividades.visi_hospi set vh_estado = 'NO-ATENDIDO' where vh_id=1