import pytest  # type: ignore
from typing import Dict
from slack_forms import forms


@pytest.fixture
def test_fields() -> Dict[str, forms.Field]:
    return {
        "button": forms.ButtonField("My Button"),
        "text": forms.TextField("My Text"),
        "checkbox": forms.CheckboxField("My Checkbox", ["check 1", "check 2"]),
        "radio_button": forms.RadioButtonField(
            "My RadioButton", ["radio 1", "radio 2"]
        ),
        "multi_select": forms.MultiSelectField(
            "My MultiSelect", ["multi 1", "multi 2"]
        ),
    }
