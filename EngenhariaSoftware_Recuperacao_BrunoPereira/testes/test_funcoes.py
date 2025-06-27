# Testes automatizados para as classes Produto, Pedido e Estoque

import unittest
from src.funcoes import Produto, Pedido, Estoque

class TestProduto(unittest.TestCase):
    def test_atualizar_estoque(self):
        produto = Produto("Granola", 20.0, 5.0)
        produto.atualizar_estoque(2.0)
        self.assertEqual(produto.quantidade_em_estoque, 7.0)

class TestPedido(unittest.TestCase):
    def test_adicionar_item_e_total(self):
        produto = Produto("Chá Verde", 30.0, 10.0)
        pedido = Pedido(1, "2025-07-10")
        pedido.adicionar_item(produto, 0.5)
        self.assertAlmostEqual(pedido.total, 15.0)
        self.assertEqual(len(pedido.itens), 1)
        self.assertEqual(produto.quantidade_em_estoque, 9.5)

class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.estoque = Estoque()
        self.produto = Produto("Semente de Chia", 50.0, 3.0)
        self.estoque.adicionar_produto(self.produto)

    def test_buscar_produto_existente(self):
        encontrado = self.estoque.buscar_produto("Semente de Chia")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nome, "Semente de Chia")

    def test_buscar_produto_inexistente(self):
        self.assertIsNone(self.estoque.buscar_produto("Castanha"))

    def test_atualizar_estoque(self):
        self.estoque.atualizar_estoque("Semente de Chia", 1.0)
        self.assertEqual(self.produto.quantidade_em_estoque, 4.0)

if __name__ == '__main__':
    unittest.main()