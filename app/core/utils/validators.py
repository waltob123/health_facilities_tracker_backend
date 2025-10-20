import re
import uuid

from email_validator import EmailNotValidError, validate_email


def is_valid_uuid(*, uuid_to_test: str, version: int = 4) -> bool:
    """Checks if an uuid is valid

    Args:
        uuid_to_test (str): The uuid to test
        version (int, optional): The uuid version. Defaults to 4.

    Returns:
        bool: True if the uuid is valid, False otherwise
    """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except (ValueError, AttributeError):
        return False

    return str(uuid_obj) == uuid_to_test


def is_valid_password(*, password: str) -> bool:
    """Checks if a password is valid

    Args:
        password (str): The password to test

    Returns:
        bool: True if the password is valid, False otherwise
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True


def is_valid_email(*, email: str) -> bool:
    """Checks if an email is valid

    Args:
        email (str): The email to test

    Returns:
        bool: True if the email is valid, False otherwise
    """
    try:
        validate_email(email)
    except EmailNotValidError:
        return False

    return True


def is_valid_telephone_number(*, phone_number: str) -> bool:
    """Validate a telephone number.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if valid otherwise False
    """
    # Regular expression pattern for country code + phone number validation
    pattern = r"^\(\d{1,3}\)(\d{7,15})$"

    # Compile regex for validation
    regex = re.compile(pattern)

    # Perform validation
    match = regex.match(phone_number)

    if match:
        return True

    return False


def is_valid_year(*, year: str) -> bool:
    """Checks if year is of the right format

    Args:
        year (str): The year to check

    Returns:
        bool: True if year is of the right format, False otherwise
    """
    return year.isdigit()
