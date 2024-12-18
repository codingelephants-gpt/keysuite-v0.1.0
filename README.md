# KeySuite V0.2.0
## About KeySuite
KeySuite is a Python module designed to generate random passkeys.
It can create passkeys using a mix of letters, numbers, and symbols or only numbers and letters based on your needs.

## Installation
1. Go to your file directory and open it in your shell
2. Run the following code:
```bash
pip install .
```
On linux execute the auto_inst_unix.py file. (you can do the same with windows)
```shell
python3 auto_inst_unix.py
```

## Commands
- newpass() - Generates a random passkey by shuffling a variety of different characters.
```python
import keysuite

print(keysuite.newpass())
# Example Output: 'G@a3Fz2*pLkT'
```
- newpass_nl() - Generates a random passkey but only uses numbers and letters.
```python
import keysuite

print(keysuite.newpass())
# Example output: 'Nm4fg7u3132Z'
```
- intro.help - A string that shows all the commands.
(The rest is located in intro.help!)


## About codingelephants-gpt
I am a single developer so there wont be a lot coming here yet.

(Dont mind all the commits, i was trying to remove bugs.)
