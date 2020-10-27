from abc import ABC, abstractmethod

class AbstractTela(ABC):
  @abstractmethod
  def __init__():
    pass

  def le_num_inteiro(self, mensagem: str, opcoes_validas: []):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if inteiro not in opcoes_validas:
          raise ValueError
        return inteiro
      except ValueError:
        print("Digite uma opção válida!")


  def verifica_inteiro(self, entidade: str):
    while True:
      valor = input()
      
      try:
        inteiro = int(valor)
        if type(inteiro) != int:
          raise ValueError

        return valor
      except ValueError:
        print(entidade ,"deve ser composto apenas de números inteiros!")


  def verifica_palavra(self):
    while True:
      valor = input()
      
      try:
        ha_numero = any(char.isdigit() for char in valor)

        if ha_numero:
          raise ValueError
        else:
          return valor
      except ValueError:
        print("Digite apenas letras!")



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