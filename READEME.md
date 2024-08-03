# AdminFinder

AdminFinder is a simple tool designed to locate admin login pages on websites. By utilizing a wordlist, this tool attempts to find various paths where the admin login page might be located.

## Features

- Easy and fast to use
- Supports both default and custom wordlists
- Displays results with color-coded status codes
- Neon effect display for tool information

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Amirprx3/AdminFinder.git
   cd AdminFinder
## Install dependencies:
Ensure you have Python installed. Then, install the necessary Python packages:
- pip install -r requirements.txt

#
# Usage
AdminFinder can be used with both default and custom wordlists.

### Using Default Wordlist
- ./adminfinder -u <target_url> -d

### Using Custom Wordlist
- ./adminfinder -u <target_url> -w <path_to_wordlist>


### Example
./adminfinder -u http://example.com -d\
./adminfinder -u http://example.com -w custom_wordlist.txt

---
# Options
-h, --help: Help to use the tool\
-u, --url: Target URL (required)\
-d, --default: Use default wordlist\
-w, --wordlist: Path to custom wordlist

---
# Output
The output will display the status of each attempted path with color-coded status codes:

- Green [200]: Found a page\
- Red [404]: Could not find the page\
- Yellow [500]: Server error

---
# Example Output
![alt image](https://github.com/user-attachments/assets/0dd26dd4-af00-4037-8f83-8a8c5d43ecfe)

# Author
Amirprx3


# License

### Additional Instructions

1. **To execute the script without .py extension:**
   - On Unix-based systems (Linux, macOS):
     ```sh
     chmod +x adminfinder
     ./adminfinder -u http://example.com -d
     ```

   - On Windows:
     Create a batch file `adminfinder.bat` with the following content:
     ```bat
     @echo off
     python path_to_script\adminfinder.py %*
     ```

2. **Ensure the batch file is in a directory included in your system's PATH.**

This `README.md` file provides comprehensive instructions on the installation, usage, and features of the `AdminFinder` tool. Feel free to customize it further as needed!
