from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    pass


  def dados_cadastro(self):
    print("Digite seu nome:")
    nome = input("")

    print("Digite seu CPF")
    cpf = input()

    print("Digite a sua senha")
    senha = input("")

    return nome, cpf, senha

  def login(self):
    
    print("Digite seu CPF")
    cpf = input()
    print("Digite sua senha")
    senha = input()

    return cpf, senha

  def remove_cliente(self):
    print("Digite seu CPF:")
    cpf = input()
    print("Digite sua senha:")
    senha = input("")

    print("Tem certeza que deseja remover o cadastro?")
    opcao = int(input())

    if opcao == 1:
      return cpf, senha
    elif opcao == 0:
      return 0, 0



  def opcoes_cliente_logado(self, nome_cliente: str):
    print("Ola", nome_cliente, "o que você deseja?")
    print("1 - Comprar")
    print("2 - Ver Cadastro")
    print("3 - Alterar Cadastro")
    print("4 - Remover Cadastro")
    print("0 - Sair")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
    return opcao

  def mostra_opcoes(self):
    print("Como cliente você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("0 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao