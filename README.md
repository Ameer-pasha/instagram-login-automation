# Instagram Login Automation

A simple Python script that automates Instagram login using Selenium WebDriver.

## ⚠️ Disclaimer

**This project is for educational purposes only.** Automating Instagram may violate their Terms of Service and could result in account restrictions. Use at your own risk and only on accounts you own.

## Prerequisites

- Python 3.6+
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/instagram-login-automation.git
   cd instagram-login-automation
   ```

2. Install dependencies:
   ```bash
   pip install selenium
   ```

3. Download [ChromeDriver](https://chromedriver.chromium.org/) and add to PATH

## Setup

1. Set environment variables:
   ```bash
   export INSTA_USERNAME="your_username"
   export INSTA_PASSWORD="your_password"
   ```

   Or create a `.env` file:
   ```
   INSTA_USERNAME=your_username
   INSTA_PASSWORD=your_password
   ```

## Usage

```bash
python main.py
```

## Features

- Automated Instagram login
- Environment variable support for credentials
- Chrome browser automation with detached mode
- Handles "Not Now" popup after login

## Security

- Never commit credentials to version control
- Use environment variables for sensitive data
- Credentials are loaded from system environment

## Legal Notice

This tool is provided for educational purposes only. Users are responsible for complying with Instagram's Terms of Service and applicable laws.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Issues

If you encounter any issues, please open a GitHub issue with:
- Python version
- Chrome version
- ChromeDriver version
- Error message (if any)