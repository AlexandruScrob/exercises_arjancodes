from observer_pattern.api.event import post_event
from observer_pattern.lib.db import create_user, find_user
from observer_pattern.lib.stringtools import get_random_string


def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)

    post_event("user_registered", user)


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    post_event("user_password_forgotten", user)
