import pytest  # type: ignore
from slack_forms import views
from .forms import test_form_class
from .fields import test_fields


@pytest.fixture
def test_modal_view_class(test_fields, test_form_class):
    class TestModalView(views.ModalView):
        title_text = 'Test'
        form_class = test_form_class

    return TestModalView


@pytest.fixture
def test_home_view_class(test_fields, test_form_class):
    class TestHomeView(views.HomeView):
        title_text = 'Test'
        form_class = test_form_class

    return TestHomeView
