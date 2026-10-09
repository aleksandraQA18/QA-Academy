import os

import pytest
from src.clients.product_client import Products
from src.factory.product_factory import create_new_product


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")


@pytest.fixture
def generate_new_product():
    payload = create_new_product()
    response = Products().create_product(payload)

    product = response.json()
    # yield product
    return product
    # products.delete_user(product["id"])
