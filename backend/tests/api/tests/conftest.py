import os

import pytest
from src.clients.product_client import Products
from src.factory.product_factory import create_new_product

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")
TEST_ENV = os.getenv("TEST_ENV", "local")  # "local" albo "stage"
READ_ONLY_METHODS = {"GET", "HEAD", "OPTIONS"}


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
