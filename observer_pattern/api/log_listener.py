from observer_pattern.lib.log import log
from observer_pattern.api.event import subscribe


def handle_user_registered_event(user):
    log(f"User registered with email address {user.email}")


def handle_user_password_forgotten_event(user):
    log(f"User with email address {user.email} requested" f" a password reset.")


def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
