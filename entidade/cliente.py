from entidade.pessoa import Pessoa

class Cliente(Pessoa):

  def __init__(self, nome: str, cpf: int, senha: str):
    self.__nome = nome
    self.__cpf = cpf
    self.__senha = senha

