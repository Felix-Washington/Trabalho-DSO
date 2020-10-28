from controlador.controlador_carrinho import ControladorCarrinho
from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_menu import ControladorMenu
from controlador.controlador_produto import ControladorProduto
from tela.tela_principal import TelaPrincipal

class ControladorPrincipal():
  def __init__(self):
    self.__controlador_cliente = ControladorCliente()
    self.__controlador_funcionario = ControladorFuncionario()
    self.__tela_principal = TelaPrincipal(self)

 
  def iniciar_sistema(self):
    self.abrir_tela_inicial()

  def mostrar_tela_funcionario(self):
    self.__controlador_funcionario.abrir_tela_inicial()

  def mostrar_tela_cliente(self):
    self.__controlador_cliente.abrir_tela_inicial()

  def finalizar_tela(self):
    exit(0)

  def abrir_tela_inicial(self):
    lista_opcoes = {
    1: self.mostra_tela_cliente,
    2: self.mostra_tela_funcionario, 
    0: self.fecha_sistema}

    while True:
      opcao_escolhida = self.__tela_menu.mostra_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()
    