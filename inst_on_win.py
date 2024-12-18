try:
	import os
	print("Installing...")
	os.system('pip install "."')
except exception as e:
	print(f'Error: {e}')
