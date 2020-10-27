from tela.abstract_tela import AbstractTela

class TelaFuncionario(AbstractTela):
  def __init__(self):
    pass

  def dados_cadastro(self):
      print("Digite seu nome:")
      nome = input("")

      print("Digite seu cpf")
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

  

  def mostra_opcoes(self):
    print("Como funcionário você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Remover Cadastro")
    print("0 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 0])
    return opcao