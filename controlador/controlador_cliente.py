from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente

class ControladorCliente(AbstractControlador):
  def __init__(self):
    self.__clientes = [] 
    self.__tela_cliente = TelaCliente()
    self.__controle = True
    self.__opcoes_controle = True
    self.__cliente_logado = None


  def abre_tela(self):
    lista_opcoes = {
    1: self.login_cliente,
    2: self.adicionar, 
    0: self.voltar}

    self.__controle = True
    while self.__controle:

      opcao_escolhida = self.__tela_cliente.mostra_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def login_cliente(self):
    cpf, senha = self.__tela_cliente.login()

    for um_cliente in self.__clientes:
      if cpf == um_cliente.cpf and senha == um_cliente.senha:
        self.__cliente_logado = um_cliente
        self.cliente_opcoes(um_cliente.nome)
        
      else:
        self.__tela_cliente.avisos("dados_invalidos", "")


  def adicionar(self):
    nome, cpf, senha = self.__tela_cliente.dados_cadastro()
    cliente = Cliente(nome, cpf, senha)
    self.__clientes.append(cliente)
    self.__tela_cliente.avisos("cadastrar", "Cliente")


  def voltar(self):
    self.__controle = False
    

  def cliente_opcoes(self, cliente):
    lista_opcoes = {
    1: self.comprar,
    2: self.ver_cadastro, 
    3: self.atualizar,
    4: self.remover,
    0: self.voltar}

    self.__opcoes_controle = True

    while self.__opcoes_controle:

      opcao_escolhida = self.__tela_cliente.opcoes_cliente_logado(cliente)

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()
  
  
  def comprar(self):
    pass


  def ver_cadastro(self):
    self.__tela_cliente.mostra_cadastro(
      self.__cliente_logado.nome,
      self.__cliente_logado.cpf,
      self.__cliente_logado.senha)


  def atualizar(self):
    opcao = self.__tela_cliente.atualiza_cadastro("")
    if opcao == 1:
      self.__cliente_logado.nome = self.__tela_cliente.atualiza_cadastro("Nome")


  def remover(self):
    cpf, senha = self.__tela_cliente.remove_cliente()
    for um_cliente in self.__clientes:
      if cpf == um_cliente.cpf and senha == um_cliente.senha:
        self.__clientes.remove(um_cliente)
        break

    self.__tela_cliente.avisos("remover", "Cliente")
    self.__opcoes_controle = False
