from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    
    pass


  def dados_cadastro(self):
    print("Digite seu nome:")
    nome = self.verifica_palavra()

    print("Digite seu CPF")
    cpf = self.verifica_inteiro("O CPF")

    print("Digite a sua senha")
    senha = input("")

    return nome, cpf, senha


  def login(self):    
    print("Digite seu CPF:")
    cpf = self.verifica_inteiro("O CPF")
    print("Digite sua senha:")
    senha = input()

    return cpf, senha


  def remove_cliente(self):
    print("Digite seu CPF:")
    cpf = self.__verifica_inteiro("O CPF")
    print("Digite sua senha:")
    senha = input("")

    print("Tem certeza que deseja remover o cadastro?")
    print("1 - Sim")
    print("2 - Não")
    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2])

    if opcao == 1:
      return cpf, senha
    elif opcao == 2:
      return 0, 0


  def atualiza_cadastro(self, valor_escolhido):
    print("O que você quer alterar?")
    print("1 - Nome")
    print("2 - Senha")
    print("0 - Voltar")
    
    opcao = input()

    if valor_escolhido == "Nome":
      print("Digite seu novo nome: ")
      nome = input()
      return nome

    elif valor_escolhido == "Senha":
      print("Digite sua nova senha:")
      senha = input()
      return senha

    elif valor_escolhido == "":
      return opcao
    

  def mostra_cadastro(self, nome, cpf, senha):
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Senha:", senha)


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