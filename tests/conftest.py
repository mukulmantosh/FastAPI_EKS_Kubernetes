import pytest

from ecommerce.user.models import User
from test_conf import override_get_db


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want

    database = next(override_get_db())
    new_user = User(name='John', email='john@gmail.com', password='john123')
    database.add(new_user)
    database.commit()

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    database.query(User).filter(User.email == 'john@gmail.com').delete()
    database.commit()
