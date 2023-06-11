CREATE DATABASE dogins;
use dogins;
CREATE TABLE pet(
	codigo varchar(50) PRIMARY KEY,
	nome_pet varchar(50),
	data_atualizacao varchar(50),
	data_cadastro varchar(50),
	nascimento varchar(50),
	idade varchar(50),
	sexo varchar(50),
	especies varchar(50),
	raca varchar(50),
	peso varchar(50),
	descricao  varchar(200)
);
select * from pet;

CREATE TABLE agendar(
	codigo varchar(50) PRIMARY KEY,
	nome_servico varchar(50),
	data_agendamento varchar(50),
	data_cadastro varchar(50),
	valor varchar(50),
	duracao varchar(50),
	descricao varchar(200),
	nome_pet varchar(50),
	codigo_pet varchar(50),
	nome_dono varchar(50)
);
select * from agendar;

CREATE TABLE dono (
    codigo_cliente varchar(50) PRIMARY KEY,
    nome_cliente varchar(50),
    data_atualizacao varchar(50),
    data_cadastro varchar(50),
    cpf varchar(50),
    data_nascimento varchar(50),
    idade varchar(50),
    telefone varchar(50),
    celular varchar(50),
    cep varchar(50),
    cidade varchar(50),
    bairro varchar(50),
    rua varchar(50)
);
select * from dono;

CREATE TABLE servicos (
    codigo_servico varchar(50) PRIMARY KEY,
    nome_servico varchar(50),
    data_atualizacao varchar(50),
    data_cadastro varchar(50),
    valor varchar(50),
    duracao varchar(50),
    descricao text
);
select * from servicos;