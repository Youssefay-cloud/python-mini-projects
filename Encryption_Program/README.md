# Encryption Program

A simple command-line encryption program written in Python. It uses a randomized substitution cipher to replace each supported character with another character.

## How It Works

1. The program creates a character set containing spaces, punctuation, digits, and upper- and lowercase letters.
2. It makes a copy of that character set and shuffles the copy to create a random encryption key.
3. Each character in the message is replaced by the character at the same position in the shuffled key.
4. The program prints the original message and its encrypted version.

Because the key is randomly shuffled each time the program starts, the same message can produce a different encrypted result on different runs. The key is kept only in memory, so an encrypted message cannot be decrypted after the program exits unless the original key is saved.

## Requirements

- Python 3.8 or newer

The program uses only Python's standard library. No additional packages are required.

## Setup and Run

From the `Encryption_Program` directory, create and activate a virtual environment:

### Linux and macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
py -m venv venv
venv\Scripts\Activate.ps1
```

Run the program:

```bash
python app.py
```

Enter a message when prompted. The program supports spaces, punctuation, digits, and English letters.

When you are finished, deactivate the virtual environment:

```bash
deactivate
```

## Current Limitation

The decryption section currently iterates over the original message instead of the encrypted input and prints the original message again. As a result, it does not yet correctly decrypt the value entered at `Enter encrypted message`.
