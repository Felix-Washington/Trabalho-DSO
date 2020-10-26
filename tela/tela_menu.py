from tela.abstract_tela import AbstractTela

class TelaMenu(AbstractTela):
  def __init__(self):
    pass

  def le_num_inteiro(self, mensagem: str = "", opcoes_validas: [] = None):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if inteiro not in opcoes_validas:
          raise ValueError
        return inteiro
      except ValueError:
        print("Digite um inteiro válido!")


  def mostra_opcoes(self):
    print("Bem vindo a loja de brinquedos Francis")
    print("Você é:")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("0 - Sair")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao