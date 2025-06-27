# Arquivo principal que executa o sistema da Grão&Cia
# Importa as classes definidas no arquivo funcoes.py
from funcoes import Produto, Pedido, Estoque

def main():
    # Cria o objeto Estoque da loja
    estoque = Estoque()

    # Cria dois produtos e define preço por kg e quantidade inicial em estoque
    cafe = Produto("Café Orgânico", 45.0, 10.0)
    castanha = Produto("Castanha-do-Pará", 70.0, 5.0)

    # Adiciona os produtos ao estoque
    estoque.adicionar_produto(cafe)
    estoque.adicionar_produto(castanha)

    # Cria um pedido com ID 1 e data de agendamento
    pedido1 = Pedido(1, "2025-07-01")

    # Adiciona itens ao pedido, com respectivas quantidades
    pedido1.adicionar_item(cafe, 0.5)        # 0.5kg de café
    pedido1.adicionar_item(castanha, 0.3)    # 0.3kg de castanha

    # Exibe resumo do pedido no terminal (itens, totais, etc.)
    pedido1.exibir_resumo()

    # Exibe relatório atualizado do estoque após o pedido
    estoque.gerar_relatorio()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()