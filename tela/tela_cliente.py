from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    pass


  def dados_cadastro(self):
    print("Digite seu nome:")
    nome = input("")

    print("Digite seu cpf")
    cpf = input()
    #cpf = self.le_num_inteiro("Escolha a opcao: ", [0,1,2,3,4,5,6,7,8,9])

    print("Digite a sua senha")
    senha = input("")

    return nome, cpf, senha

  def tela_login(self):
    dados_usuario = []
    print("Digite seu CPF")
    dados_usuario.append(input(" "))

    return dados_usuario

  def avisos(self, opcao):
    if opcao == "cadastrar":
      print("Usuário cadastrado com sucesso!")
    elif opcao == "remover":
      print("Usuário removido com sucesso!")