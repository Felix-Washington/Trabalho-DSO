from entidade.pessoa import Pessoa

class Funcionario(Pessoa):

  def __init__(self):
    self.__nome = " "
    pass

  @property
  def nome(self):
    return self.__nome