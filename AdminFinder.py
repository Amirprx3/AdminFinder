import os
import sys
import time
import argparse
import random
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import httpx
from bs4 import BeautifulSoup  # To extract the page title

try:
    import urllib3; urllib3.disable_warnings()
except ImportError:
    os.system('pip install urllib3')

try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install beautifulsoup4')
    from bs4 import BeautifulSoup

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

neonEffect(
    f'''
{g}     ___      __        _        ____ _          __         
{g}    / _ | ___/ /__ _   (_)___   / __/(_)___  ___/ /___  ____
{w}   / __ |/ _  //  ' \ / // _ \ / _/ / // _ \/ _  // -_)/ __/
{r}  /_/ |_|\_,_//_/_/_//_//_//_//_/  /_//_//_/\_,_/ \__//_/   
{p} -----------------------------------------------------------
  {g}Version | 2.0 - Advanced Admin Panel Finder
  {w}MadeBy: @Amirprx3
  {r}GitHub: https://github.com/Amirprx3
{p} -----------------------------------------------------------
{w}
'''
)

def validate_url(url):
    if len(url) < 5:
        raise ValueError("URL is too short!")

def load_proxies(proxy_file):
    try:
        with open(proxy_file, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"{r}[!] Error reading the proxies file: {e}{w}")
        return []

def test_proxy(proxy):
    client = None
    try:
        client = httpx.Client(verify=False, follow_redirects=True, proxies={"http://": proxy, "https://": proxy})
        response = client.get("https://www.google.com", headers=get_random_headers(), timeout=5)
        if response.status_code == 200:
            print(f"{g}[*] Proxy {proxy} is working{w}")
            return True
        else:
            print(f"{y}[!] Proxy {proxy} failed (Status: {response.status_code}){w}")
            return False
    except Exception as e:
        print(f"{y}[!] Proxy {proxy} failed: {e}{w}")
        return False
    finally:
        if client is not None:
            client.close()

def filter_proxies(proxies_list):
    working_proxies = [proxy for proxy in proxies_list if test_proxy(proxy)]
    print(f"{w}[*] Found {len(working_proxies)} working proxies out of {len(proxies_list)}{w}")
    return working_proxies

def get_page_title(content):
    try:
        soup = BeautifulSoup(content, 'html.parser')
        return soup.title.string.strip() if soup.title else ""
    except:
        return ""

def is_404_page(content, base_content, base_title, base_length, response_url, original_url, headers):
    content_lower = content.lower()
    content_length = len(content)
    page_title = get_page_title(content)

    # Checking 404 words
    if any(keyword in content_lower for keyword in ["404", "not found", "page not found", "error 404"]):
        return True
    
    # If redirected to the home page
    if response_url != original_url and response_url == base_url:
        return True
    
    # If the page title is the same as the home page
    if page_title and page_title == base_title and "location" not in headers:
        return True
    
    # If the content length is similar to the home page and is not a redirect
    if abs(content_length - base_length) < 100 and "location" not in headers:
        return True
    
    return False

def is_admin_page(content):
    content_lower = content.lower()
    admin_keywords = ["login", "admin", "dashboard", "cpanel", "administrator", "adminlogin"]
    has_login_form = any(tag in content_lower for tag in ["<input type=\"password\">", "<form", "username"])
    return any(keyword in content_lower for keyword in admin_keywords) and has_login_form

def get_random_headers():
    ua = UserAgent()
    return {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Referer': f'https://www.google.com/search?q={random.randint(1, 1000)}',
        'DNT': '1'
    }

def determine_protocol(base_url, retries=1):
    client = httpx.Client(verify=False, follow_redirects=True)
    try:
        for attempt in range(retries + 1):
            try:
                test_url = f"https://{base_url}"
                response = client.get(test_url, headers=get_random_headers(), timeout=15)
                if response.status_code < 400:
                    print(f"{w}[*] Using HTTPS for {base_url}{w}")
                    return "https://"
                elif response.status_code in [301, 302]:
                    redirect_url = response.headers.get('location', '')
                    if redirect_url.startswith('http'):
                        protocol = redirect_url.split('://')[0] + "://"
                        print(f"{w}[*] Redirected to {protocol} for {base_url}{w}")
                        return protocol
            except Exception as e:
                print(f"{y}[!] HTTPS attempt {attempt + 1} failed for {base_url}: {e}{w}")
            
            try:
                test_url = f"http://{base_url}"
                response = client.get(test_url, headers=get_random_headers(), timeout=15)
                if response.status_code < 400:
                    print(f"{w}[*] Using HTTP for {base_url}{w}")
                    return "http://"
                elif response.status_code in [301, 302]:
                    redirect_url = response.headers.get('location', '')
                    if redirect_url.startswith('http'):
                        protocol = redirect_url.split('://')[0] + "://"
                        print(f"{w}[*] Redirected to {protocol} for {base_url}{w}")
                        return protocol
            except Exception as e:
                print(f"{y}[!] HTTP attempt {attempt + 1} failed for {base_url}: {e}{w}")
            
            if attempt < retries:
                time.sleep(2)
        
        print(f"{r}[!] Could not determine protocol for {base_url} after {retries + 1} attempts{w}")
        sys.exit(1)
    finally:
        client.close()

def scan_path(args):
    path, full_url, proxies_list, base_content, base_title, base_length, base_url = args
    test_url = f"{full_url}/{path}"
    proxy = random.choice(proxies_list) if proxies_list else None
    client = httpx.Client(verify=False, follow_redirects=True, proxies={"http://": proxy, "https://": proxy} if proxy else None)
    try:
        response = client.get(test_url, headers=get_random_headers(), timeout=10)
        status_code = response.status_code
        content = response.text
        headers = response.headers
        final_url = str(response.url) # Final URL after redirect

        if status_code == 403 or status_code == 429:
            return f"{y}[!] Blocked by WAF or rate limit - URL: {test_url} (Proxy: {proxy or 'None'}){w}"
        elif 'cf-ray' in headers or 'cloudflare' in content.lower():
            return f"{y}[!] Cloudflare detected - URL: {test_url}{w}"

        if status_code < 400:
            if is_404_page(content, base_content, base_title, base_length, final_url, test_url, headers):
                return f'[{r}404{w}] Page not found (disguised as 200) - URL: {test_url}'
            elif is_admin_page(content):
                return f'[{g}{status_code}{w}] Found a potential admin page - URL: {test_url} (Proxy: {proxy or 'None'})'
            else:
                return f'[{y}{status_code}{w}] Page found but not an admin page - URL: {test_url}'
        elif 400 <= status_code < 500:
            return f'[{r}{status_code}{w}] Could not find page - URL: {test_url}'
        elif status_code >= 500:
            return f'[{y}{status_code}{w}] Server error - URL: {test_url}'
    except Exception as e:
        return f"{r}[!] Error reaching {test_url}: {e} (Proxy: {proxy or 'None'}){w}"
    finally:
        client.close()

# Argument parser
parser = argparse.ArgumentParser(description='AdminFinder Ultimate - Advanced Admin Panel Finder')
parser.add_argument('-u', '--url', required=True, help='Target URL (with or without http:// or https://)')
parser.add_argument('-d', '--default', action='store_true', help='Use default wordlist')
parser.add_argument('-w', '--wordlist', help='Path to custom wordlist')
parser.add_argument('-p', '--proxy', help='Single proxy (http://user:pass@host:port or socks5://...)')
parser.add_argument('-pf', '--proxyfile', help='Path to proxy list file')
parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads (default: 10)')

args = parser.parse_args()
url = args.url
use_default = args.default
wordlist_path = args.wordlist
proxy = args.proxy
proxy_file = args.proxyfile
threads = args.threads

try:
    validate_url(url)
except ValueError as e:
    print(f"{r}[!] Error: {e}{w}")
    sys.exit(1)

print(f"{w}[*] URL provided: {url}")

# Determine protocol if not provided
if not url.startswith('http://') and not url.startswith('https://'):
    protocol = determine_protocol(url)
    full_url = f"{protocol}{url}"
else:
    full_url = url

# Test URL reachability and get base content
client = httpx.Client(verify=False, follow_redirects=True)
try:
    test = client.get(full_url, headers=get_random_headers(), timeout=15)
    test.raise_for_status()
    base_content = test.text
    base_length = len(base_content)
    base_title = get_page_title(base_content)
    base_url = full_url
    print(f"{w}[*] Successfully reached the URL: {full_url}")
except Exception as e:
    print(f"{r}[!] Error reaching the URL: {e}{w}")
    sys.exit(1)
finally:
    client.close()

# Load proxies
proxies_list = load_proxies(proxy_file) if proxy_file else ([proxy] if proxy else [])
if proxies_list:
    proxies_list = filter_proxies(proxies_list)
    if not proxies_list:
        print(f"{y}[!] No working proxies found. Continuing without proxies...{w}")
else:
    print(f"{y}[!] No proxies provided. Using direct connection{w}")

time.sleep(2)

# Load wordlist
default_wordlist_path = 'wordlist.txt'
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
    print(f"{r}[!] Please use -d or --default or provide a custom wordlist with -w{w}")
    sys.exit(1)

print(f"{g}<-----------------------------START----------------------------->{w}\n")

# Scan with multithreading
try:
    with ThreadPoolExecutor(max_workers=threads) as executor:
        scan_args = [(path, full_url, proxies_list, base_content, base_title, base_length, base_url) for path in wordlist]
        results = executor.map(scan_path, scan_args)
        for result in results:
            print(result)
            time.sleep(random.uniform(0.05, 0.3))
except KeyboardInterrupt:
    print(f"{r}[!] Interrupted by user. Exiting...{w}")
    sys.exit(0)

print(f"{g}<-----------------------------FINISHED----------------------------->{w}")
# made by: Amirprx3
