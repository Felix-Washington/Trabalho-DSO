from abc import ABC, abstractmethod

class Pessoa(ABC):
  @abstractmethod
  def __init__(self, nome, cpf, senha):
    pass

  @abstractmethod
  def nome(self):
    pass