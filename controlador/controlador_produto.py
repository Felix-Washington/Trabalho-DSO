from controlador.abstract_controlador import AbstractControlador
from tela.tela_produto import TelaProduto

class ControladorProduto(AbstractControlador):
  def __init__(self):
    self.__tela_produto = TelaProduto(self)
    self.__produtos = []
  
  def iniciar (self):
    pass

  def add (self):
    pass

  def remover (self):
    pass

  def atualizar (self):
    pass

  def listar(self):
    pass

  def abrir_tela_inicial(self):
    pass
    
  def finalizar_tela(self):
    pass

  def relatorio_estoque(self):
    pass

  def atualizar_estoque(self):
    pass
    
  def imprimir_relatorio(self):
    pass
    
  @property
  def produtos(self):
    return self.__produtos
