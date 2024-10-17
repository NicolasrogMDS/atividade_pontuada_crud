from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base 
from os import system
from time import sleep
system("cls||clear")

dados = []
#Criando Banco de dados:
BD = create_engine("sqlite:///bancodedados.db")

#Conectando ao banco de dados:
Session = sessionmaker(bind=BD)
session = Session()

#Criando Tabela e Classe:
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "usuarios"
    
    #Definindo variaveis da tabela:
    i = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    sobrenome = Column("Sobrenome", String)
    idade = Column("Idade", Integer)
    peso = Column("Peso", Float)
    altura = Column("Altura", Float)
    sexo = Column("Sexo", String)
    #Duvida: Como fazer para declarar sub classes. 
    #Ex: Professor > Alunos > Pais
    #E como fazer para acessar elas através da classe principal "Professor"

    #Definindo atributos da classe:
    def __init__(self,nome:str, sobrenome:str, idade:int,peso:float,altura:float,sexo:str):
        self.nome = nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.sexo=sexo                                                                                                                                    

#Criando tabela de dados, no banco de dados:
Base.metadata.create_all(bind=BD)    