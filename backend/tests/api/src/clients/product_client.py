import requests


class Products:
    def __init__(self):
        self.url = "api/products"

    def get_all_products(self, base_url):
        """Get all products"""
        response = requests.get(f"{base_url}/{self.url}")
        return response

    def get_product_by_id(self, base_url, product_id):
        """Get product by Id"""
        response = requests.get(f"{base_url}/{self.url}/{product_id}")
        return response

    def create_product(self, base_url, payload):
        """Create new product"""
        response = requests.post(f"{base_url}/{self.url}", json=payload)
        return response
