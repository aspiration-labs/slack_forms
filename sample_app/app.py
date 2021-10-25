import os
import sys
from slack_bolt import App
from slack_forms import views, forms, logging


try:
    app_token = os.environ["SLACK_BOT_TOKEN"]
    app_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
except KeyError:
    print(
        "Set SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET env vars for your app.\n"
        "See https://api.slack.com/authentication/basics for more information"
    )
    sys.exit(1)


# slack-forms provides a json logger, or use the slack_bolt loggers or your own
logger = logging.getLogger(__name__)


# Initializes your app with your bot token and signing secret
app = App(
    token=app_token,
    signing_secret=app_signing_secret,
)


class PizzaOrderForm(forms.Form):

    size = forms.RadioButtonField(
        label="Pizza Size:", options=["slice", "small", "medium", "large"]
    )
    toppings = forms.MultiSelectField(
        label="Pizza Toppings",
        options=["pepperoni", "onions", "sausage", "bell peppers"],
        optional=True,
    )
    extras = forms.CheckboxField(
        label="Extras",
        options=["Parmesan", "Red Pepper", "Napkins", "Yellow Peppers"],
        optional=True,
    )
    special_requests = forms.TextField(
        label="Special Requests",
        placeholder="Anything else about your order?",
        optional=True,
        multiline=True,
    )


class PizzaOrderView(views.ModalView):

    title_text = "Pizza Order"
    form_class = PizzaOrderForm

    def form_valid(self, form: forms.Form):
        print(form.data)


class HomeForm(forms.Form):

    pizza_order_button = forms.ButtonField(text="Order a Pizza")


class HomeView(views.HomeView):

    form_class = HomeForm

    def pizza_order_button_action(self, ack, body, client, view):
        ack()
        view = PizzaOrderView(self.app).render()
        try:
            client.views_open(
                trigger_id=body["trigger_id"],
                view=view,
            )
        except Exception as e:
            logger.error(f"Error opening view: {e}", extra={"props": {"view": view}})


@app.event("app_home_opened")
def app_home_opened_action(client, event):
    view = HomeView(app).render()
    try:
        client.views_publish(
            user_id=event["user"],
            view=view,
        )
    except Exception as e:
        logger.error(f"Error opening view: {e}", extra={"props": {"view": view}})


# Start your app
if __name__ == "__main__":
    port = os.environ.get("PORT", 3000)
    app.start(port=int(port))
