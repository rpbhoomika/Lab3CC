# from products import dao
# 
# 
# class Product:
#     def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.cost = cost
#         self.qty = qty
# 
#     def load(data):
#         return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])
# 
# 
# def list_products() -> list[Product]:
#     products = dao.list_products()
#     result = []
#     for product in products:
#         result.append(Product.load(product))
#     
#     return result
# 
# 
# 
# def get_product(product_id: int) -> Product:
#     return Product.load(dao.get_product(product_id))
# 
# 
# def add_product(product: dict):
#     dao.add_product(product)
# 
# 
# def update_qty(product_id: int, qty: int):
#     if qty < 0:
#         raise ValueError('Quantity cannot be negative')
#     dao.update_qty(product_id, qty)
# 
# 
#
from dataclasses import dataclass
from products import dao


@dataclass
class Product:
    id: int
    name: str
    description: str
    cost: float
    qty: int = 0

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Fetches and returns all products."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches a product by ID."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found")
    return Product.load(product_data)


def add_product(product: dict):
    """Adds a new product after validation."""
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product):
        raise ValueError(f'Missing required product keys: {required_keys - product.keys()}')
    if not isinstance(product['cost'], (int, float)) or product['cost'] < 0:
        raise ValueError('Cost must be a non-negative number')
    if not isinstance(product['qty'], int) or product['qty'] < 0:
        raise ValueError('Quantity must be a non-negative integer')
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    if not dao.get_product(product_id):
        raise ValueError(f'Product with ID {product_id} does not exist')
    dao.update_qty(product_id, qty)
