# !/usr/bin/env python3

import os
import sys
import time
import argparse

try:
    import urllib3; urllib3.disable_warnings()
except ImportError:
    os.system('pip install urllib3')

try:
    import requests as req
except ImportError:
    os.system('pip install requests')

os.system('clear' if os.name == 'posix' else 'cls')

# Define color codes
r = '\033[31m'  # Red
g = '\033[32m'  # Green
b = '\033[36m'  # Blue
p = '\033[35m'  # Purple
w = '\033[0m'   # White
y = "\033[1;33;40m"  # Yellow

def neonEffect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)

# Display script information with neon effect
neonEffect(
    f'''
{g}     ___      __        _        ____ _          __         
{g}    / _ | ___/ /__ _   (_)___   / __/(_)___  ___/ /___  ____
{w}   / __ |/ _  //  ' \ / // _ \ / _/ / // _ \/ _  // -_)/ __/
{r}  /_/ |_|\_,_//_/_/_//_//_//_//_/  /_//_//_/\_,_/ \__//_/   

{p} -----------------------------------------------------------
  {g}Version | 1.0
  {w}MadeBy: @Amirprx3
  {r}GitHub: https://github.com/Amirprx3
{p} -----------------------------------------------------------

'''
)

def validate_url(url):
    if len(url) < 5:
        raise ValueError("URL is too short!")

# Set up argument parser
parser = argparse.ArgumentParser(description='AdminFinder - A tool to find admin panels')
parser.add_argument('-u', '--url', required=True, help='Target URL')
parser.add_argument('-d', '--default', action='store_true', help='Use default wordlist')
parser.add_argument('-w', '--wordlist', help='Path to custom wordlist')

# Parse arguments
args = parser.parse_args()
url = args.url
use_default = args.default
wordlist_path = args.wordlist

try:
    validate_url(url)
except ValueError as e:
    print(f"{r}[!] Error: {e}{w}")
    sys.exit(1)

print(f"{w}[*] URL provided: {url}")

# Check if the URL contains 'http://' or 'https://'
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

# Make a GET request to the URL
try:
    test = req.get(url, verify=False)
    test.raise_for_status()
    print(f"{w}[*] Successfully reached the URL: {url}")
except req.exceptions.RequestException as e:
    print(f"{r}[!] Error reaching the URL: {e}{w}")
    sys.exit(1)

# Delay for 5 seconds
time.sleep(5)

url = url.replace('http://', '').replace('https://', '')

# Default wordlist file path
default_wordlist_path = 'wordlist.txt'

# Load wordlist
if use_default:
    try:
        with open(default_wordlist_path, 'r', encoding='utf-8') as file:
            wordlist = [line.strip() for line in file.readlines()]
        print(f"{w}[*] Using default wordlist from: {default_wordlist_path}{w}\n")
    except Exception as e:
        print(f"{r}[!] Error reading the default wordlist file: {e}{w}")
        sys.exit(1)
elif wordlist_path:
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            wordlist = [line.strip() for line in file.readlines()]
        print(f"{g}[*] Using custom wordlist from: {wordlist_path}{w}\n")
    except Exception as e:
        print(f"{r}[!] Error reading the wordlist file: {e}{w}")
        sys.exit(1)
else:
    print(f"{r}[!] Please use -d or --default to use the default wordlist or provide a custom wordlist with -w or --wordlist{w}")
    sys.exit(1)

print(f"{g}<------------------------START------------------------>{w}\n")

for path in wordlist:
    test_url = f"http://{url}/{path}"

    try:
        response = req.get(test_url, verify=False)
        status_code = response.status_code

        if status_code < 400 or status_code == 200:
            print(f'[{g}{status_code}{w}] Found a page - URL: {test_url}')
        elif 400 <= status_code < 500:
            print(f'[{r}{status_code}{w}] Could not find page - URL: {test_url}')
        elif status_code >= 500:
            print(f'{y}[{status_code}{w}] Server error - URL: {test_url}')

    except req.exceptions.RequestException as e:
        print(f"{r}[!] Error reaching {test_url}: {e}{w}")

#made by: @Amirprx3
