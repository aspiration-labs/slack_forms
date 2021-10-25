#!/usr/bin/env python

from typing import Dict, Any
from slack_forms import views
from ..fixtures.slack import slack_app
from ..fixtures.views import test_modal_view_class, test_home_view_class
from ..fixtures.forms import test_form_class
from ..fixtures.fields import test_fields


def get_element(block: Dict[str, Any]) -> str:
    if block['type'] == 'actions':
        return block['elements'][0]['type']
    elif block['type'] == 'input':
        return block['element']['type']
    else:
        raise Exception(f'cannot test for block type {block["type"]}')


def test_modal_render(slack_app, test_fields, test_form_class, test_modal_view_class):
    view: views.ModalView = test_modal_view_class(slack_app)
    rendered = view.render()
    types = [get_element(block) for block in rendered['blocks']]

    assert types == ['button', 'plain_text_input', 'checkboxes', 'radio_buttons', 'multi_static_select']


def test_home_render(slack_app, test_fields, test_form_class, test_home_view_class):
    view: views.ModalView = test_home_view_class(slack_app)
    rendered = view.render()
    types = [get_element(block) for block in rendered['blocks']]

    assert types == ['button', 'plain_text_input', 'checkboxes', 'radio_buttons', 'multi_static_select']
