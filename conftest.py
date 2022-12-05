import pytest

from src.event import Event


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
def event_init():
    if not hasattr(pytest, "event"):
        pytest.event = Event()
    yield
    del pytest.event

@pytest.fixture
def invalidate_access_token():
    pytest.event.access_token = (pytest.config['INVALID_ACCESS_TOKEN']).replace("\n", "")
    yield
    pytest.event.access_token = (pytest.config['ACCESS_TOKEN']).replace("\n", "")