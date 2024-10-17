import logging as logger
import random
import string

def generate_random_email_and_username(domain=None, email_prefix=None):
    logger.debug("Generating random email and username.")

    if not domain:
        domain = "example.test"
    if not email_prefix:
        email_prefix = "testuser_"

    random_email_string_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + random_string + "@" + domain

    username = random_string

    random_info = {"email": email, "username": username}

    logger.debug(f"Random email and username: {random_info}")

    return random_info