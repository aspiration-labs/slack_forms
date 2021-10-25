import pytest  # type: ignore
from slack_bolt import App


@pytest.fixture
def slack_app():
    return App()
