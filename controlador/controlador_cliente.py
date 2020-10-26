from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente

class ControladorCliente(AbstractControlador):
  def __init__(self):
    self.__clientes = [] 
    self.__tela_cliente = TelaCliente()
    self.__controle = True
    pass

  def login_cliente(self):
    self.__tela_cliente.login_cliente()
    

  def adicionar(self):
    nome, cpf, senha = self.__tela_cliente.dados_cadastro()
    cliente = Cliente(nome, cpf, senha)
    self.__clientes.append(cliente)
    self.__tela_cliente.avisos("cadastrar")


  def remover(self):
    
    pass
    #self.__tela_cliente.avisos("remover")

  def voltar(self):
    self.__controle = False
    

  def abre_tela(self):
    lista_opcoes = {
    1: self.login_cliente,
    2: self.adicionar, 
    3: self.remover,
    0: self.voltar}

    while self.__controle:

      opcao_escolhida = self.__tela_cliente.mostra_opcoes("cliente", [1, 2, 3, 0])

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()