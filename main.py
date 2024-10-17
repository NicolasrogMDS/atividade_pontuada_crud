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
    cpf = Column(String, primary_key=True)
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

def menu_principal ():
    print("""   === RH System ===
        1 - Adicionar um funcionário
        2 - Consultar um funcionário
        3 - Atualizar os dados de um funcionário
        4 - Excluir um funcionário
        5 - Listar todos os funcionários
        0 - Sair do sistema.
        """)

def limpar_tela():
    system("cls||clear")
    sleep(2)

def logo_empresa():
    print("="*20)
    print(f"{"SENAI":^20}")
    print("="*20)

def listar_todos_funcionarios(a):
    for funcionario in a:
        print(f"\n{funcionario.nome, funcionario.sobrenome} - {funcionario.idade} - {funcionario.cpf}")
        print(f"{funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone} - {funcionario.sexo}")
        sleep(2)

while True:
    while True:
        menu_principal()
        opcao = int(input(": "))
        if opcao == 1 or 2 or 3 or 4 or 5 or 0:
            break
    match (opcao):
        case 1:
            while True:
                limpar_tela()
                logo_empresa()
                funcionario = Funcionario(
                    nome = input("Insira o nome: "),
                    sobrenome = input("Insira o sobrenome: "),
                    idade = int(input("Insira a idade: ")),
                    cpf = input("Insira o CPF: "),
                    setor = input("Insira o setor: "),
                    funcao = input("Insira a função: "),
                    salario = float(input("Insira o salário: ")),
                    telefone = input("Insira o telefone: "),
                    sexo = input("Insira o sexo (M/F ): ")
                )
                session.add(funcionario)
                session.commit
                lista_funcionarios = session.query(Funcionario).all()
                opcao1 = int(input("Deseja adicionar outro funcionario ? \n1- Sim\n2- Não"))
                if opcao1 == 2:
                    break
        case 2:
            cpf_funcionario = input("Informe o CPF do funcionario desejado: ")
            pesquisar_funcionario = session.query(Funcionario).filter_by(funcionario.cpf == cpf_funcionario).first()
            print(f"Nome e sobrenome: {funcionario.nome, funcionario.sobrenome}")
            print(f"Idade: {funcionario.idade}")
            print(f"CPF: {funcionario.cpf}")
            print(f"Setor: {funcionario.setor}")
            print(f"Função: {funcionario.funcao}")
            print(f"Salário: {funcionario.salario}")
            print(f"Telefone: {funcionario.telefone}")
            print(f"Sexo: {funcionario.sexo}")
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Todos os funcionários:")
            listar_todos_funcionarios(lista_funcionarios)