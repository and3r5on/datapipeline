CREATE TABLE ASSOCIADO(
    id int primary key,
    nome varchar,
    sobrenome varchar,
    idade int,
    email varchar
);


CREATE TABLE CONTA(
    id int primary key,
    tipo int, --para o primeiro instante sera um int de 1 a 9.
    data_criacao timestamp,
    id_associado int,
    foreign key (id_associado) references ASSOCIADO(id)
);


CREATE TABLE CARTAO (
    id int primary key,
    num_cartao int,
    nom_impresso varchar(100),
    id_conta int,
    id_associado int,
    foreign key (id_conta) references CONTA (id),
    foreign key (id_associado) references ASSOCIADO(id)
);


CREATE TABLE MOVIMENTO (
    id int primary key,
    vlr_transacao decimal(10,2),
    des_transacao varchar,
    data_movimentacao timestamp,
    id_cartao int,
    foreign key (id_cartao) references cartao(id)
);

