try:
	import os
	print("Enter your password here for security reasons:")
	os.system('sudo apt install "pip"')
	os.system('pip install "."')
except exception as e:
	print(f'Error: {e}')


