from tela.abstract_tela import AbstractTela

class TelaFuncionario(AbstractTela):
  def __init__(self):
    pass

  def dados_cadastro(self):
      print("Digite seu nome:")
      nome = self.verifica_palavra()

      print("Digite seu cpf")
      cpf = self.verifica_inteiro("O CPF")

      print("Digite a sua senha")
      senha = input("")

      return nome, cpf, senha


  def login(self):
    print("Digite seu CPF")
    cpf = self.verifica_inteiro("O CPF")
    print("Digite sua senha")
    senha = input()

    return cpf, senha


  def remove_funcionario(self):
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

  
  def desloga_funcionario(self):
    print("Tem certeza que deseja sair?")
    print("1 - Sim")
    print("2 - Não")
    opcao = self.__le_num_inteiro("", [1, 2])

    return opcao


  def opcoes_funcionario_logado(self, nome_funcionario: str):
    print("Ola", nome_funcionario, "o que você deseja?")
    print("1 - Ver Estoque")
    print("2 - Ver Cadastro")
    print("3 - Alterar Cadastro")
    print("4 - Remover Cadastro")
    print("0 - Sair")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
    return opcao


  def mostra_opcoes(self):
    print("Como funcionário você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("0 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao