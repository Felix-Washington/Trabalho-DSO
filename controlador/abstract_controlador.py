from abc import ABC, abstractmethod

class AbstractControlador(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def adicionar():
    pass

  @abstractmethod
  def remover():
    pass

  @abstractmethod
  def atualizar():
    pass