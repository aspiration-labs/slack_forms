import pytest  # type: ignore
from typing import Dict, Callable


class MockSlackBoltApp:

    view_handlers: Dict[str, Callable] = {}
    action_handlers: Dict[str, Callable] = {}

    def view(self, callback_id):
        def set_handler(handler: Callable):
            self.view_handlers[callback_id] = handler

        return set_handler

    def action(self, action_id):
        def set_handler(handler: Callable):
            self.action_handlers[action_id] = handler

        return set_handler


@pytest.fixture
def slack_app():
    return MockSlackBoltApp()
