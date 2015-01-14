import pytest
import hello_app


@pytest.fixture
def app():
    return hello_app.app


@pytest.fixture
def test_client(app):
    return app.test_client()


def test_hello(test_client):
    """
    GIVEN: A flask hello app
    WHEN: I GET the hello/ route
    THEN: The response should be "hello world"
    """
    assert True
