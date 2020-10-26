from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    pass


def opcoes_cadastro(self):
  dados_usuario = []
  print("Digite seu nome:")
  dado = input("")
  dados_usuario.append(dado)

  print("Digite seu cpf")
  dado = input("")
  dados_usuario.append(dado)

  print("Digite a sua senha")
  dado = input("")
  dados_usuario.append(dado)

  return dados_usuario