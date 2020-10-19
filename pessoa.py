import abc, abstractmethod

class Pessoa(abc):
  @abstractmethod
  def __init__(self, nome, cpf, senha):
    pass

  @abstractmethod
  def nome(self):
    pass