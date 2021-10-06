from observer_pattern.lib.slack import post_slack_message
from observer_pattern.api.event import subscribe


def handle_user_registered_event(user):
    post_slack_message("sales", f"{user.name} has registered with email"
                                f"address {user.email}")


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
