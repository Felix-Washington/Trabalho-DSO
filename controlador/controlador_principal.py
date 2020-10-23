from controlador.controlador_carrinho import ControladorCarrinho
from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_menu import ControladorMenu
from controlador.controlador_produto import ControladorProduto

from tela.tela_carrinho import TelaCarrinho
from tela.tela_cliente import TelaCliente
from tela.tela_funcionario import TelaFuncionario
from tela.tela_menu import TelaMenu
from tela.tela_produto import TelaProduto

class ControladorPrincipal():
  def __init__(self):
    
    self.__controlador_carrinho = ControladorCarrinho
    self.__controlador_cliente = ControladorCliente
    self.__controlador_funcionario = ControladorFuncionario
    self.__controlador_menu = ControladorMenu
    self.__controlador_produto = ControladorProduto

    self.__tela_carrinho = TelaCarrinho
    self.__tela_cliente = TelaCliente
    self.__tela_funcionario = TelaFuncionario
    self.__tela_menu = TelaMenu
    self.__tela_produto = TelaProduto


  def inicia_sistema(self):
    self.abre_tela()
    pass

  def abre_tela(self):
    #self.__tela_menu.mostra_opcoes(self)

    pass