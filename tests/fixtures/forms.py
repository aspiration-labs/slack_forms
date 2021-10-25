import pytest  # type: ignore
from typing import Type, Any, Dict
from slack_forms import forms
from .fields import test_fields


@pytest.fixture
def test_form_class(test_fields) -> Type[forms.Form]:
    class TestForm(forms.Form):
        button = test_fields["button"]
        text = test_fields["text"]
        checkbox = test_fields["checkbox"]
        radio_button = test_fields["radio_button"]
        multi_select = test_fields["multi_select"]

    return TestForm


@pytest.fixture
def test_form_view_data() -> Dict[str, Any]:
    """Captured from TestForm run"""

    return {
        "id": "V02GHRFSNDP",
        "team_id": "T025D39CRFF",
        "type": "modal",
        "blocks": [
            {
                "type": "actions",
                "block_id": "hxF=e",
                "elements": [
                    {
                        "type": "button",
                        "action_id": "button-action",
                        "text": {
                            "type": "plain_text",
                            "text": "My Button",
                            "emoji": True,
                        },
                    }
                ],
            },
            {
                "type": "input",
                "block_id": "text",
                "label": {"type": "plain_text", "text": "My Text", "emoji": True},
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "text-action",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter text",
                        "emoji": True,
                    },
                    "multiline": False,
                    "dispatch_action_config": {
                        "trigger_actions_on": ["on_enter_pressed"]
                    },
                },
            },
            {
                "type": "input",
                "block_id": "checkbox",
                "label": {"type": "plain_text", "text": "My Checkbox", "emoji": True},
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "checkboxes",
                    "action_id": "checkbox-action",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "check 1",
                                "emoji": True,
                            },
                            "value": "check 1",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "check 2",
                                "emoji": True,
                            },
                            "value": "check 2",
                        },
                    ],
                },
            },
            {
                "type": "input",
                "block_id": "radio-button",
                "label": {
                    "type": "plain_text",
                    "text": "My RadioButton",
                    "emoji": True,
                },
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "radio_buttons",
                    "action_id": "radio-button-action",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "radio 1",
                                "emoji": True,
                            },
                            "value": "radio 1",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "radio 2",
                                "emoji": True,
                            },
                            "value": "radio 2",
                        },
                    ],
                },
            },
            {
                "type": "input",
                "block_id": "multi-select",
                "label": {
                    "type": "plain_text",
                    "text": "My MultiSelect",
                    "emoji": True,
                },
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "multi_static_select",
                    "action_id": "multi-select-action",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select items",
                        "emoji": True,
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "multi 1",
                                "emoji": True,
                            },
                            "value": "multi 1",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "multi 2",
                                "emoji": True,
                            },
                            "value": "multi 2",
                        },
                    ],
                },
            },
        ],
        "private_metadata": "",
        "callback_id": "7c6edd55-771b-45dc-ac67-73431b69d032",
        "state": {
            "values": {
                "text": {
                    "text-action": {"type": "plain_text_input", "value": "some text"}
                },
                "checkbox": {
                    "checkbox-action": {
                        "type": "checkboxes",
                        "selected_options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "check " "1",
                                    "emoji": True,
                                },
                                "value": "check " "1",
                            }
                        ],
                    }
                },
                "radio-button": {
                    "radio-button-action": {
                        "type": "radio_buttons",
                        "selected_option": {
                            "text": {
                                "type": "plain_text",
                                "text": "radio " "1",
                                "emoji": True,
                            },
                            "value": "radio " "1",
                        },
                    }
                },
                "multi-select": {
                    "multi-select-action": {
                        "type": "multi_static_select",
                        "selected_options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "multi " "1",
                                    "emoji": True,
                                },
                                "value": "multi " "1",
                            }
                        ],
                    }
                },
            }
        },
        "hash": "1632964086.MNKl1Hdu",
        "title": {"type": "plain_text", "text": "Test", "emoji": True},
        "clear_on_close": False,
        "notify_on_close": False,
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit", "emoji": True},
        "previous_view_id": None,
        "root_view_id": "V02GHRFSNDP",
        "app_id": "A0275CT13NU",
        "external_id": "",
        "app_installed_team_id": "T025D39CRFF",
        "bot_id": "B026UCJGQ01",
    }


@pytest.fixture
def test_form_body_data() -> Dict[str, Any]:
    return {
        "type": "view_submission",
        "team": {"id": "T025D39CRFF", "domain": "aspirationeng-yvu5018"},
        "user": {
            "id": "U025NA0DH6G",
            "username": "rmorison",
            "name": "rmorison",
            "team_id": "T025D39CRFF",
        },
        "api_app_id": "A0275CT13NU",
        "token": "Uc9rD8v3dUGtSQroDfYQ18Z7",
        "trigger_id": "2549248017059.2183111433525.63a83adba6d7d2a75c1c0a4645b7f852",
        "view": {
            "id": "V02GHRFSNDP",
            "team_id": "T025D39CRFF",
            "type": "modal",
            "blocks": [
                {
                    "type": "actions",
                    "block_id": "hxF=e",
                    "elements": [
                        {
                            "type": "button",
                            "action_id": "button-action",
                            "text": {
                                "type": "plain_text",
                                "text": "My Button",
                                "emoji": True,
                            },
                        }
                    ],
                },
                {
                    "type": "input",
                    "block_id": "text",
                    "label": {"type": "plain_text", "text": "My Text", "emoji": True},
                    "optional": False,
                    "dispatch_action": False,
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "text-action",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Enter text",
                            "emoji": True,
                        },
                        "multiline": False,
                        "dispatch_action_config": {
                            "trigger_actions_on": ["on_enter_pressed"]
                        },
                    },
                },
                {
                    "type": "input",
                    "block_id": "checkbox",
                    "label": {
                        "type": "plain_text",
                        "text": "My Checkbox",
                        "emoji": True,
                    },
                    "optional": False,
                    "dispatch_action": False,
                    "element": {
                        "type": "checkboxes",
                        "action_id": "checkbox-action",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "check 1",
                                    "emoji": True,
                                },
                                "value": "check 1",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "check 2",
                                    "emoji": True,
                                },
                                "value": "check 2",
                            },
                        ],
                    },
                },
                {
                    "type": "input",
                    "block_id": "radio-button",
                    "label": {
                        "type": "plain_text",
                        "text": "My RadioButton",
                        "emoji": True,
                    },
                    "optional": False,
                    "dispatch_action": False,
                    "element": {
                        "type": "radio_buttons",
                        "action_id": "radio-button-action",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "radio 1",
                                    "emoji": True,
                                },
                                "value": "radio 1",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "radio 2",
                                    "emoji": True,
                                },
                                "value": "radio 2",
                            },
                        ],
                    },
                },
                {
                    "type": "input",
                    "block_id": "multi-select",
                    "label": {
                        "type": "plain_text",
                        "text": "My MultiSelect",
                        "emoji": True,
                    },
                    "optional": False,
                    "dispatch_action": False,
                    "element": {
                        "type": "multi_static_select",
                        "action_id": "multi-select-action",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select items",
                            "emoji": True,
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "multi 1",
                                    "emoji": True,
                                },
                                "value": "multi 1",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "multi 2",
                                    "emoji": True,
                                },
                                "value": "multi 2",
                            },
                        ],
                    },
                },
            ],
            "private_metadata": "",
            "callback_id": "7c6edd55-771b-45dc-ac67-73431b69d032",
            "state": {
                "values": {
                    "text": {
                        "text-action": {
                            "type": "plain_text_input",
                            "value": "some text",
                        }
                    },
                    "checkbox": {
                        "checkbox-action": {
                            "type": "checkboxes",
                            "selected_options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "check " "1",
                                        "emoji": True,
                                    },
                                    "value": "check " "1",
                                }
                            ],
                        }
                    },
                    "radio-button": {
                        "radio-button-action": {
                            "type": "radio_buttons",
                            "selected_option": {
                                "text": {
                                    "type": "plain_text",
                                    "text": "radio " "1",
                                    "emoji": True,
                                },
                                "value": "radio " "1",
                            },
                        }
                    },
                    "multi-select": {
                        "multi-select-action": {
                            "type": "multi_static_select",
                            "selected_options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "multi " "1",
                                        "emoji": True,
                                    },
                                    "value": "multi " "1",
                                }
                            ],
                        }
                    },
                }
            },
            "hash": "1632964086.MNKl1Hdu",
            "title": {"type": "plain_text", "text": "Test", "emoji": True},
            "clear_on_close": False,
            "notify_on_close": False,
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "submit": {"type": "plain_text", "text": "Submit", "emoji": True},
            "previous_view_id": None,
            "root_view_id": "V02GHRFSNDP",
            "app_id": "A0275CT13NU",
            "external_id": "",
            "app_installed_team_id": "T025D39CRFF",
            "bot_id": "B026UCJGQ01",
        },
        "response_urls": [],
        "is_enterprise_install": False,
        "enterprise": None,
    }
