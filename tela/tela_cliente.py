from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
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

  def tela_login(self):
    
    print("Digite seu CPF")
    cpf = input()
    print("Digite sua senha")
    senha = input()

    return cpf, senha

