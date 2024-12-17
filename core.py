import random as rng
import string
def newpass():
	num = rng.randint(0, 99999999)
	
	num = str(num).zfill(8)
		
	length = 8
	
	letters = string.ascii_letters + string.digits
	full_ltr = ''.join(rng.choices(letters, k=length))
	
	
	password = num + full_ltr
	
	password_list = list(password)
	rng.shuffle(password_list)
	shuffled_password = ''.join(password_list)
	
	return shuffled_password
	
print(newpass())
	

"""
Password Generator in python

PROPERTY OF codingelephants-gpt ON https://github.com/codingelephants-gpt/pgen1.0.0
"""
