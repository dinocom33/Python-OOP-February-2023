from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [str, None]:
        try:
            current_product = next(filter(lambda p: p.name == product_name, self.products))
        except StopIteration:
            return None

        return current_product

    def remove(self, product_name: str) -> None:
        curr_product = self.find(product_name)

        if curr_product:
            self.products.remove(curr_product)

    def __repr__(self) -> str:
        return "\n".join(f"{p}: {p.quantity}" for p in self.products)
