# KeySuite V0.1.5
## About KeySuite
KeySuite is a Python module designed to generate random passkeys.
It can create passkeys using a mix of letters, numbers, and symbols or only numbers and letters based on your needs.

## Installation
1. Go to your file directory and open it in your shell
2. Run the following code:
```bash
pip install .
```
   Or on linux:
```bash
sudo apt install .
```
## Commands
- newpass() - Generates a random passkey by shuffling a variety of different characters.
```python
import keysuite

print(keysuite.newpass())
# Example Output: G@a3Fz2*pLkT
```
- newpass_nl() - Generates a random passkey but only uses numbers and letters.
```python
import keysuite

print(keysuite.newpass())
# Example output: 'Nm4fg7u3132Z'
```


## About codingelephants-gpt
I am a single developer so there wont be a lot coming here yet.

(Dont mind all the commits, i was trying to remove bugs.)
