# Classes principais do sistema: Produto, Pedido e Estoque
# Classe que representa um produto vendido a granel
class Produto:
    def __init__(self, nome: str, preco_por_kg: float, quantidade_em_estoque: float):
        # Nome do produto
        self.nome = nome
        # Preço do produto por quilograma
        self.preco_por_kg = preco_por_kg
        # Quantidade atual em estoque (em kg)
        self.quantidade_em_estoque = quantidade_em_estoque

    # Atualiza a quantidade em estoque (pode aumentar ou reduzir)
    def atualizar_estoque(self, qtd: float):
        self.quantidade_em_estoque += qtd

    # Exibe os dados do produto no terminal
    def exibir_dados(self):
        print(f"Produto: {self.nome}")
        print(f"Preço por Kg: R${self.preco_por_kg:.2f}")
        print(f"Estoque disponível: {self.quantidade_em_estoque:.2f} Kg")


# Classe que representa um pedido feito por um cliente
class Pedido:
    def __init__(self, id_pedido: int, agendado_para: str):
        # ID único do pedido
        self.id_pedido = id_pedido
        # Lista de itens no pedido (tuplas de Produto e quantidade)
        self.itens = []
        # Total em reais do pedido
        self.total = 0.0
        # Data/hora agendada para retirada do pedido
        self.agendado_para = agendado_para

    # Adiciona um item (produto e quantidade) ao pedido
    def adicionar_item(self, produto: Produto, qtd: float):
        self.itens.append((produto, qtd))
        # Calcula subtotal e adiciona ao total do pedido
        self.total += produto.preco_por_kg * qtd
        # Atualiza estoque do produto, retirando a quantidade vendida
        produto.atualizar_estoque(-qtd)

    # Retorna o valor total do pedido
    def calcular_total(self):
        return self.total

    # Exibe no terminal um resumo completo do pedido
    def exibir_resumo(self):
        print(f"\nPedido #{self.id_pedido} - Retirada: {self.agendado_para}")
        for produto, qtd in self.itens:
            print(f"{produto.nome} - {qtd}kg x R${produto.preco_por_kg:.2f}")
        print(f"Total: R${self.total:.2f}")


# Classe que representa o estoque da loja
class Estoque:
    def __init__(self):
        # Lista com todos os produtos disponíveis
        self.produtos = []

    # Adiciona um novo produto ao estoque
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    # Busca um produto pelo nome e retorna o objeto correspondente
    def buscar_produto(self, nome: str):
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                return p
        return None

    # Atualiza a quantidade de um produto específico
    def atualizar_estoque(self, nome: str, qtd: float):
        produto = self.buscar_produto(nome)
        if produto:
            produto.atualizar_estoque(qtd)
            print(f"Estoque de '{nome}' atualizado com sucesso.")
        else:
            print(f"Produto '{nome}' não encontrado.")

    # Gera e exibe um relatório com todos os produtos e seus estoques
    def gerar_relatorio(self):
        print("\nRelatório de Estoque:")
        for produto in self.produtos:
            produto.exibir_dados()