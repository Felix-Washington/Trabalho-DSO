from entidade.pessoa import Pessoa

class Cliente(Pessoa):

  def __init__(self, nome, cpf, senha, ):
    self.__nome = nome
    self.__cpf = cpf
    self.__senha = senha

  @property
  def nome(self):
    return self.__nome