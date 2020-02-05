--tabla idiomas
create table referenciales.idiomas(idi_id serial primary key, idi_des varchar(100) not null unique);

insert into referenciales.idiomas(idi_des)values('ESPAÑOL'),('INGLES'),('ALEMAN');