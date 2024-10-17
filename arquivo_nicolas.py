from os import system


print("""   === RH System ===
1 - Adicionar um funcionário
2 - Consultar um funcionário
3 - Atualizar os dados de um funcionário
4 - Excluir um funcionário
5 - Listar todos os funcionários
0 - Sair do sistema.
""")
# O menu deverá ser exibido após utilizar uma das suas opções

def limpar_terminal():
    system("cls || clear")