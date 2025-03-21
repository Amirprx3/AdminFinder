[فارسی](#ادمین-فایندر)

# AdminFinder

AdminFinder is an advanced tool designed to locate admin login pages on websites. By leveraging a wordlist, multithreading, and smart detection techniques, this tool efficiently scans for potential admin panel paths.



## Features

- **Fast and Efficient:** Utilizes multithreading for rapid scanning.
- **Smart 404 Detection:** Identifies disguised 404 pages using content analysis, title comparison, and redirect checks.
- **Proxy Support:** Supports HTTP and SOCKS proxies for anonymity.
- **Flexible Wordlists:** Works with both default and custom wordlists.
- **Color-Coded Output:** Displays results with clear, color-coded status codes.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Amirprx3/AdminFinder.git
   cd AdminFinder

### Install Dependencies:
Ensure you have Python 3 installed. Then, install the required packages:
  ```bash
  pip install -r requirements.txt
  ```
#### Required packages:
- `httpx[socks]`
- `fake-useragent`
- `beautifulsoup4`

# Usage

AdminFinder supports various options for scanning websites.
### Using Default Wordlist
```bash
python adminfinder.py -u <target_url> -d
```
### Using Custom Wordlist
```bash
python adminfinder.py -u <target_url> -w <path_to_wordlist>
```
### Using Proxies
```bash
python adminfinder.py -u <target_url> -d -pf <proxy_file>
```
## Example Commands
```bash
python adminfinder.py -u http://example.com -d -t 20
python adminfinder.py -u http://example.com -w custom_wordlist.txt -pf proxies.txt
```

# Options
- `-u, --url`: Target URL (required)
- `-d, --default`: Use default wordlist
- `-w, --wordlist`: Path to custom wordlist
- `-p, --proxy`: Single proxy (e.g., `http://user:pass@host:port` or `socks5://host:port`)
- `-pf, --proxyfile`: Path to proxy list file
- `-t, --threads`: Number of threads (default: 10)

# Output

The output displays the status of each path with color-coded indicators:

- **Green [200]**: Found a potential admin page
- **Red [404]**: Page not found (includes disguised 200s)
- **Yellow [500]**: Server error
- **Yellow [!]**: Warnings (e.g., WAF detection, Cloudflare)

## Example Output
```
[*] URL provided: http://example.com
[*] Successfully reached the URL: http://example.com
[*] Using default wordlist from: wordlist.txt

<-----------------------------START----------------------------->

[404] Page not found (disguised as 200) - URL: http://example.com/admin1.php
[200] Found a potential admin page - URL: http://example.com/admin/login.php
[500] Server error - URL: http://example.com/server.php
[!] Blocked by WAF - URL: http://example.com/adm/
```
# Author
Developed by [Amirprx3](https://github.com/Amirprx3).

# License
This project is open-source and available under the MIT License.

# Additional Instructions
1. To Execute Without .py Extension:
    - Unix-based Systems (Linux, macOS):
    ```bash
    chmod +x adminfinder
    ./adminfinder -u http://example.com -d
    ```
2. Proxy File Format: Example `proxies.txt`:
    ```
    http://60.187.75.70:8085
    socks5://117.74.65.207:80
    ```


# ادمین فایندر

ابزار AdminFinder یه ابزار پیشرفته‌ست که برای پیدا کردن صفحات ورود ادمین توی وب‌سایت‌ها طراحی شده. این ابزار با استفاده از وردلیست، چندنخی و تکنیک‌های تشخیص هوشمند، مسیرهای احتمالی پنل ادمین رو با سرعت بالا اسکن می‌کنه.

## ویژگی‌ها
- `سریع و کارآمد`: از چندنخی برای اسکن سریع استفاده می‌کنه.
- `تشخیص هوشمند 404`: صفحات 404 جعلی رو با تحلیل محتوا، مقایسه عنوان و بررسی ریدایرکت‌ها تشخیص می‌ده.
- `پشتیبانی از پراکسی`: از پراکسی‌های HTTP و SOCKS برای ناشناس موندن پشتیبانی می‌کنه.
- `وردلیست انعطاف‌پذیر`: با وردلیست پیش‌فرض و سفارشی کار می‌کنه.
- `خروجی رنگی`: نتایج رو با کدهای وضعیت رنگی واضح نشون می‌ده.

# نصب
## دریافت مخزن:
```bash
git clone https://github.com/Amirprx3/AdminFinder.git
cd AdminFinder
```
## نصب پیش‌نیازها:
مطمئن شو که پایتون 3 نصب داری. بعد بسته‌های مورد نیاز رو نصب کن:
```bash
pip install -r requirements.txt
```
### بسته‌های لازم:
- `httpx[socks]`
- `fake-useragent`
- `beautifulsoup4`

# نحوه استفاده
AdminFinder گزینه‌های مختلفی برای اسکن وب‌سایت‌ها داره.
### استفاده از وردلیست پیش‌فرض
```bash
python adminfinder.py -u <target_url> -d
```
### استفاده از وردلیست سفارشی
```bash
python adminfinder.py -u <target_url> -w <path_to_wordlist>
```
### استفاده از پراکسی
```bash
python adminfinder.py -u <target_url> -d -pf <proxy_file>
```
## مثال دستورات
```bash
python adminfinder.py -u http://example.com -d -t 20
python adminfinder.py -u http://example.com -w custom_wordlist.txt -pf proxies.txt
```

# گزینه‌ها
- `-u, --url`: آدرس هدف (اجباری)
- `-d, --default`: استفاده از وردلیست پیش‌فرض
- `-w, --wordlist`: مسیر وردلیست سفارشی
- `-p, --proxy`: یه پراکسی تکی (مثل, `http://user:pass@host:port` یا `socks5://host:port`)
- `-pf, --proxyfile`: مسیر فایل لیست پراکسی
- `-t, --threads`: تعداد نخ‌ها (پیش‌فرض: 10)

# خروجی
خروجی وضعیت هر مسیر رو با رنگ‌های مشخص نشون می‌ده:
- `سبز [200]`: یه صفحه ادمین احتمالی پیدا شده
- `قرمز [404]`: صفحه پیدا نشده (شامل 200های جعلی)
- `زرد [500]`: خطای سرور
- `زرد [!]`: هشدارها (مثل تشخیص WAF یا Cloudflare)

## نمونه خروجی
```
[*] URL provided: http://example.com
[*] Successfully reached the URL: http://example.com
[*] Using default wordlist from: wordlist.txt

<-----------------------------START----------------------------->

[404] Page not found (disguised as 200) - URL: http://example.com/admin1.php
[200] Found a potential admin page - URL: http://example.com/admin/login.php
[500] Server error - URL: http://example.com/server.php
[!] Blocked by WAF - URL: http://example.com/adm/
```

# سازنده

ساخته شده توسط [Amirprx3](https://github.com/Amirprx3)

# مجوز
این پروژه متن‌بازه و تحت مجوز MIT در دسترسه.

# دستورالعمل‌های اضافی
1. اجرای اسکریپت بدون پسوند .py:
    - سیستم‌های یونیکس (لینوکس، مک):
    ```bash
    chmod +x adminfinder
    ./adminfinder -u http://example.com -d
    ```
2. فرمت فایل پراکسی: نمونه `proxies.txt`:
    ```bash
    http://60.187.75.70:8085
    socks5://117.74.65.207:80
    ```