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
    def __init__(self,nome:str, sobrenome:str,idade:int, cpf:str, setor:str,funcao:str,salario:float,telefone:str,sexo:str):
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

while True:
    while True:
        print("""   === RH System ===
        1 - Adicionar um funcionário
        2 - Consultar um funcionário
        3 - Atualizar os dados de um funcionário
        4 - Excluir um funcionário
        5 - Listar todos os funcionários
        0 - Sair do sistema.
        """)
        opcao = int(input(": "))
        if opcao == 1 or 2 or 3 or 4 or 5 or 0:
            break
    match (opcao):
        case 1:
            while True:
                funcionario = Funcionario(
                    nome = input("Insira o nome: "),
                    sobre = input("Insira o sobrenome: "),
                    idade = int(input("Insira a idade: ")),
                    cpf = input("Insira o CPF: "),
                    setor = input("Insira o setor: "),
                    funcao = input("Insira a função: "),
                    salario = float("Insira o salário: "),
                    telefone = input("Insira o telefone: "),
                    sexo = ("Insira o sexo (M/F ): ")
                )
                session.add(funcionario)
                session.commit
                opcao1 = int(input("Deseja adicionar outro funcionario ? \n1- Sim\n2- Não"))
                if opcao1 == 2:
                    break
        case 2:
            
        case 3:
        case 4:
        case 5:
        case 0: