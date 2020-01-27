import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Test default product weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        prod = Product('Test Product', price=10, weight=20)
        self.assertEqual(prod.stealability(), 'Kinda Stealable')

    def test_explode(self):
        prod = Product('Test Product', weight=20, flammability=0.5)
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme report is correct"""

    def test_default_num_products(self):
        product = generate_products()
        self.assertEqual(len(product), 30)

    def test_legal_name(self):
        products = generate_products()
        self.assertIn(products[0], "Awesome Anvil")


if __name__ == '__main__':
    unittest.main()
