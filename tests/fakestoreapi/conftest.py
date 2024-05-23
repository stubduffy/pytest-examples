import pytest
from helpers.fakestore_client import FakeStoreClient


@pytest.fixture(scope="session")
def fakestore_client():
    return FakeStoreClient("https://fakestoreapi.com")
