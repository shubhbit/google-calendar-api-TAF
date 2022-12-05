import pytest


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