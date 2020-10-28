
class TelaPrincipal:
    def __init__(self, controlador):
      self.__controlador = controlador
    def opcoes(self):

      print("------ COMO DESEJA LOGAR ------")
      print("1 - Funcionário")
      print("2 - Cliente")
      print("0 - Finalizar Sistema")
    
      opcao = self.le_numero_inteiro("Escolha a opção: ")
      return opcao