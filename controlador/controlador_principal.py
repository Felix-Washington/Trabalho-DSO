from controlador.controlador_carrinho import ControladorCarrinho
from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_menu import ControladorMenu
from controlador.controlador_produto import ControladorProduto

from tela.tela_menu import TelaMenu


class ControladorPrincipal():
  def __init__(self):
    
    self.__controlador_carrinho = ControladorCarrinho()
    self.__controlador_cliente = ControladorCliente()
    self.__controlador_funcionario = ControladorFuncionario()
    self.__controlador_menu = ControladorMenu()
    self.__controlador_produto = ControladorProduto()

    self.__tela_menu = TelaMenu()



  def inicia_sistema(self):
    self.abre_tela()
    pass

  def mostra_tela_funcionario(self):
    pass

  def mostra_tela_cliente(self):
    self.__controlador_cliente.controle = True
    self.__controlador_cliente.abre_tela()


  def fecha_sistema(self):

    exit(0)

  def abre_tela(self):
    lista_opcoes = {1: self.mostra_tela_cliente,
    2: self.mostra_tela_funcionario, 
    0: self.fecha_sistema}

    while True:
  

      opcao_escolhida = self.__tela_menu.mostra_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()
    