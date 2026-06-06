#!/usr/bin/env python3
import argparse
import subprocess
import sys

def try_password(password, gpg_file):
    try:
        result = subprocess.run(
            [
                "gpg", "--batch", "--yes", "--passphrase", password,
                "--pinentry-mode", "loopback", "-d", gpg_file,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            timeout=10,
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def main():
    parser = argparse.ArgumentParser(description="Brute-force GPG file decryption")
    parser.add_argument("gpg_file", help="Path to the .gpg file to decrypt")
    parser.add_argument("wordlist", help="Path to the passwords wordlist file")
    args = parser.parse_args()

    with open(args.wordlist, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]

    total = len(passwords)
    print(f"Loaded {total} passwords from {args.wordlist}")

    for i, pw in enumerate(passwords, 1):
        if i % 100 == 0:
            print(f"\r  tried {i}/{total} ...", end="", flush=True)
        if try_password(pw, args.gpg_file):
            print(f"\n[+] Password found: {pw}  (attempt #{i})")
            sys.exit(0)

    print(f"\n[-] No password found after {total} attempts.")

if __name__ == "__main__":
    main()
