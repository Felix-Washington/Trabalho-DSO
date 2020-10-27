from controlador.abstract_controlador import AbstractControlador
from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario(AbstractControlador):
  def __init__(self):
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()
    self.__controle = True
    

  def login_funcionario(self):
    self.__tela_funcionario.login()
    pass

  def adicionar(self):
    nome, cpf, senha = self.__tela_funcionario.dados_cadastro()
    funcionario = Funcionario(nome, cpf, senha)
    self.__funcionarios.append(funcionario)
    self.__tela_funcionario.avisos("cadastrar", "Funcionário")
    
    pass

  def remover(self):
    pass

  def voltar(self):
    self.__controle = False


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