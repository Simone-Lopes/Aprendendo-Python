create database Totem;
use Totem;

#Número de totens e id que vai identifica-los
create table totens (
idTotens int primary key auto_increment,
nome varchar(40)
);

insert into totens values
	(null, "Totem1"),
    (null, "Totem2"),
    (null, "Totem3");

#Valores serão inseridos nessa tabela
create table liltotem (
idTotem int primary key auto_increment,
processador decimal(10,2),
memoria decimal(10,2),
disco decimal(10,2),
SO varchar(40),
fkTotens int,
constraint fkTotens
foreign key (fkTotens) references totens(idTotens)
);

#Visualizar tabela
select * from liltotem;


