# core.py
import random
import string
def newpass(length=12):
	"""Generate a random password."""
	characters = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(characters) for _ in range(length))

def newpass_nl(length=12):
	key_num = str(random.randint(0, 999999)).zfill(6)
	key_string = ''.join(random.choices(string.ascii_letters, k=6))
	key = key_num + key_string
	key_list = list(key)
	random.shuffle(key_list)
	return ''.join(key_list)
