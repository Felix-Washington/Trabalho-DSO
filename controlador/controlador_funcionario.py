from controlador.abstract_controlador import AbstractControlador
from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario(AbstractControlador):
  def __init__(self):
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()
    self.__controle = True
    self.__funcionario_logado = None

    self.__log_funcionario = False


  def login_funcionario(self):
    cpf, senha = self.__tela_funcionario.login()
    
    for um_funcionario in self.__funcionarios:
      if cpf ==um_funcionario.cpf and senha == um_funcionario.senha:
        self.__funcionario_logado = um_funcionario
        self.__log_funcionario = True
        self.__tela_funcionario.opcoes_funcionario_logado(um_funcionario.nome) 
      else:
        self.__tela_funcionario.avisos("dados_invalidos", "")

  def adicionar(self):
    nome, cpf, senha = self.__tela_funcionario.dados_cadastro()
    funcionario = Funcionario(nome, cpf, senha)
    self.__funcionarios.append(funcionario)
    self.__tela_funcionario.avisos("cadastrar", "Funcionário")
    

  def remover(self):
    cpf, senha = self.__tela_funcionario.remove_funcionario()
    for um_funcionario in self.__funcionarios:
      if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
        self.__funcionarios.remove(um_funcionario)
        break

    self.__tela_funcionario.avisos("remover", "Funcionario")
    self.__opcoes_controle = False


  def ver_estoque(self):
    pass


  def ver_cadastro(self):
    self.__funcionario_logado.nome
    self.__funcionario_logado.cpf
    self.__funcionario_logado.senha


  def atualizar(self):
    pass


  def deslogar(self):
    opcao = self.__tela_funcionario.desloga_funcionario()
    if opcao == 1:
      self.__log_funcionario = False


  def funcionario_opcoes(self, funcionario):
    lista_opcoes = {
    1: self.ver_estoque,
    2: self.ver_cadastro, 
    3: self.atualizar,
    4: self.remover,
    0: self.deslogar}

    while self.__log_funcionario:

      opcao_escolhida = self.__tela_funcionario.opcoes_funcionario_logado(funcionario)
      print(self.__log_funcionario)
      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def abre_tela(self):
    lista_opcoes = {
    1: self.login_funcionario,
    2: self.adicionar, 
    3: self.remover,
    0: self.voltar}

    self.__controle = True
    while self.__controle:

      opcao_escolhida = self.__tela_funcionario.mostra_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def voltar(self):
    pass
    #self.__controle = False