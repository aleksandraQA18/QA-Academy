import requests
from config import TEST_URL


class Products:
    def __init__(self):
        self.url = "api/products"

    def get_all_products(self):
        """Get all products"""
        response = requests.get(f"{TEST_URL}/{self.url}")
        return response

    def get_product_by_id(self, product_id):
        """Get product by Id"""
        response = requests.get(f"{TEST_URL}/{self.url}/{product_id}")
        return response

    def create_product(self, payload):
        """Create new product"""
        response = requests.post(f"{TEST_URL}/{self.url}", json=payload)
        return response
