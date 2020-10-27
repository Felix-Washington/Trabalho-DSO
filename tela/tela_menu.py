from tela.abstract_tela import AbstractTela

class TelaMenu(AbstractTela):
  def __init__(self):
    pass


  def mostra_opcoes(self):
    print("Bem vindo a loja de brinquedos Francis")
    print("Você é:")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("0 - Sair")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao