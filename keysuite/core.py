# core.py

def newpass(length=12):
    """Generate a random password."""
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
