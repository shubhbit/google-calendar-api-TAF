import pytest

from src.event import Event


def pytest_addoption(parser):
    parser.addoption(
        '--access-token', action='store', default='token', help='Access token'
    )


@pytest.fixture(scope="session", autouse=True)
def access_token(request):
    return request.config.getoption('--access-token')


@pytest.fixture(scope="session", autouse=True)
def read_config():
    if not hasattr(pytest, "config"):
        pytest.config = {}
    with open("config.env", "r") as f:
        for line in f:
            line = line.split("=")
            pytest.config[line[0]] = line[1]
    yield
    del pytest.config


@pytest.fixture(scope="module", autouse=True)
def event_init(access_token):
    if not hasattr(pytest, "event"):
        pytest.event = Event(access_token)
    yield
    del pytest.event


@pytest.fixture
def invalidate_access_token(access_token):
    pytest.event._access_token = (
        pytest.config['INVALID_ACCESS_TOKEN']).replace("\n", "")
    yield
    pytest.event._access_token = access_token
