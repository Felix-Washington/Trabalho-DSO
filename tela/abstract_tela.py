from abc import ABC, abstractmethod

class AbstractTela(ABC):
  @abstractmethod
  def __init__():
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
    print("Você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Remover Cadastro")
    print("0 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao