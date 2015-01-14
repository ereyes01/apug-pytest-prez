import pytest
import hello_app


MOCK_ENCODING = "mock-encoding"


class MockEncodingResponse:
    def __init__(self):
        self.headers = {"Content-Encoding": MOCK_ENCODING}


def _mock_get(url):
    assert url == "https://news.ycombinator.com"
    return MockEncodingResponse()


@pytest.fixture
def mock_encoding_request(monkeypatch):
    monkeypatch.setattr("requests.get", _mock_get)


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
    response = test_client.get("/hello")
    assert response.data.decode("utf-8") == "hello world"


def test_encoding_header(test_client, mock_encoding_request):
    """
    GIVEN: A flask hello app
           A mock request handler
    WHEN: I GET the /hacker_news_encoding route
    THEN: The response should be the expected Content-Encoding
    """
    response = test_client.get("/hacker_news_encoding")
    assert response.data.decode("utf-8") == MOCK_ENCODING
