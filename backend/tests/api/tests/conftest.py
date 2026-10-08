import pytest
from src.clients.product_client import Products
from src.factory.product_factory import create_new_product


@pytest.fixture
def generate_new_product():
    payload = create_new_product()
    response = Products().create_product(payload)

    product = response.json()
    # yield product
    return product
    # products.delete_user(product["id"])
