from controlador.abstract_controlador import AbstractControlador

from tela_carrinho import TelaCarrinho

class ControladorCarrinho(AbstractControlador):

  def __init__(self):
    self.__tela_carrinho = TelaCarrinho(self)
    self.__carrinhos = []

  def iniciar (self):
    pass

  def listar(self):
    pass

  def add (self):
    pass

  def remover (self):
    pass

  def limpar_carrinho(self):
    pass
    
  def valor_total(self):
    pass

  def finalizar_tela(self):
    pass

  def abrir_tela_inicial(self):
    pass



  