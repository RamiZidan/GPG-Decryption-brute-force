# GPG Brute-Force Decryption Tool

A simple Python script to brute-force decrypt a GPG-encrypted file using a password wordlist.

## Requirements

- Python 3.6+
- [GnuPG](https://gnupg.org/) (`gpg`) installed and available in `PATH`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python bruteforce_gpg.py <gpg_file> <wordlist>
```

- `gpg_file` — Path to the `.gpg` encrypted file
- `wordlist` — Path to a text file containing candidate passwords (one per line)

### Example

```bash
python bruteforce_gpg.py secret.gpg rockyou.txt
```

## How It Works

The script reads passwords from the wordlist and attempts to decrypt the GPG file with each one by calling `gpg --batch --yes --passphrase <pw> -d <file>`. It stops as soon as a successful decryption is found.

Progress is printed every 100 attempts.

## License

MIT
