from tela.abstract_tela import AbstractTela

class TelaCarrinho(AbstractTela):
  def __init__(self):
    pass



  def mostra_opcoes(self):
    print("Você deseja:")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Limpar Carrinho")
    print("0 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opcao: ")
    return opcao
