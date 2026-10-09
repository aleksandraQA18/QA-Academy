import logging
from decimal import Decimal

from faker import Faker

logging.getLogger("faker").setLevel(logging.WARNING)


fake = Faker()


def create_new_product():
    product_price = Decimal(
        str(fake.pydecimal(left_digits=2, right_digits=2, positive=True))
    )
    return {
        "name": f"QA Course {fake.random_int(min=1000, max=9999)}",
        "description": fake.text(max_nb_chars=200),
        "category": fake.random_element(
            elements=[
                "ISTQB",
                "QA Courses",
                "Automation",
                "API Testing",
                "Performance Testing",
            ]
        ),
        "price": float(product_price),
    }
