from abc import ABC, abstractmethod

class AbstractControlador(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def adicionar(self):
    pass

  #@abstractmethod
  def remover(self):
    pass

  #@abstractmethod
  def atualizar(self):
    pass