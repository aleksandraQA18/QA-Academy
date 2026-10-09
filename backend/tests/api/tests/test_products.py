import pytest
from config import LOG
from src.clients.product_client import Products
from src.factory.product_factory import create_new_product


@pytest.mark.smoke
def test_get_all_products():
    LOG.info("test_get_all_products")
    response = Products().get_all_products()
    response_json = response.json()
    LOG.debug(response_json)

    assert response.ok


@pytest.mark.smoke
def test_get_product_by_id(generate_new_product):
    LOG.info("test_get_product_by_id")
    response = Products().get_product_by_id(generate_new_product["id"])
    response_json = response.json()
    LOG.debug(response_json)

    assert response.ok
    assert response_json["id"] == generate_new_product["id"]


def test_create_new_product():
    LOG.info("test_create_new_product")

    payload = create_new_product()

    LOG.debug(payload)
    response = Products().create_product(payload)
    response_json = response.json()
    LOG.debug(response_json)

    assert response.ok


# To add
# -> negative tests
# -> edge cases
