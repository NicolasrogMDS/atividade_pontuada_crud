from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base 
from os import system
from time import sleep
system("cls||clear")

dados = []
#Criando Banco de dados:
BD = create_engine("sqlite:///EmpresaSenaibancodedados.db")

#Conectando ao banco de dados:
Session = sessionmaker(bind=BD)
session = Session()

#Criando Tabela e Classe:
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    #Definindo variaveis da tabela:
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    sobrenome = Column(String)
    idade = Column(Integer)
    cpf = Column(String)
    setor = Column(String)
    funcao = Column(String)
    salario = Column(Float)
    telefone = Column(String)
    sexo = Column(String)

    #Definindo atributos da classe:
    def __init__(self,nome:str, sobrenome:str,idade:int, cpf:str, setor:str,funcao:str,salario:str,telefone:str,sexo:str):
        self.nome = nome
        self.sobrenome=sobrenome
        self.idadade = idade                                                                                            
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        self.sexo = sexo                                     

#Criando tabela de dados, no banco de dados:
Base.metadata.create_all(bind=BD)
    