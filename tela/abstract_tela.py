from abc import ABC, abstractmethod

class AbstractTela(ABC):
  @abstractmethod
  def __init__():
    pass

  @abstractmethod
  def le_num_inteiro():
    pass

  def mostra_opcoes():
    print("Você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Remover Cadastro")
    print("0 - Voltar")

    