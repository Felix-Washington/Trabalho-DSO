from controlador.abstract_controlador import AbstractControlador

class ControladorProduto(AbstractControlador):
  def __init__(self):
    #self.__produtos = [] = None
    pass

  def adicionar(self):
    pass

  @property
  def produtos(self):
    return self.__produtos

  @produtos.setter
  def produtos(self, produtos):
    self.__produtos = produtos