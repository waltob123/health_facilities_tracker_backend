def generate_secret_key(*, number_of_bytes: int = 32) -> str:
    """Generate a secure random secret key.

    Args:
        number_of_bytes (int, optional): Number of bytes for the key. Defaults to 32.

    Returns:
        str: A URL-safe base64-encoded string representing the secret key.
    """
    import secrets

    return secrets.token_urlsafe(nbytes=number_of_bytes)
