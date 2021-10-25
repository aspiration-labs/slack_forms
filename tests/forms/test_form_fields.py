#!/usr/bin/env python

from ..fixtures.fields import test_fields
from ..fixtures.forms import test_form_class


def test_declared_fields(test_fields, test_form_class):
    test_form = test_form_class()
    assert test_form.declared_fields == test_fields
