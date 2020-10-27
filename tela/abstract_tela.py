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

  @abstractmethod
  def mostra_opcoes(self):
    pass



  def avisos(self, opcao: str, entidade: str):
    if opcao == "cadastrar":
      print(entidade, "cadastrado com sucesso!")
    elif opcao == "remover":
      print(entidade, "removido com sucesso!")
    elif opcao == "dados_invalidos":
      print("Erro! Digite o cpf ou a senha corretamente!")