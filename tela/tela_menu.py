from tela.abstract_tela import AbstractTela

class TelaMenu(AbstractTela):
  def __init__(self):
    pass

  def le_num_inteiro(self, opcoes_validas: []):
    while True:
      dado_usuario = int(input())
      try:
        if dado_usuario not in opcoes_validas:
          raise ValueError


      except ValueError:
        print("Digite um inteiro válido!")


  def mostra_opcoes(self):
    print("Bem vindo a loja de brinquedos Francis")
    print("Você é:")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("0 - Sair")

    opcao = self._le_num_inteiro([0,1,2])