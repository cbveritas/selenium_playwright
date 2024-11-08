# Selenium and Playwrigth basic script

This project provides two Python scripts that scrape flight information from LATAM's website for flights from Bogotá (BOG) to Cartagena (CTG). Both scripts demonstrate the use of two popular web scraping frameworks: Selenium and Playwright.

# Overview

1. **selenium_script.py**: Uses Selenium with ChromeDriver to load the LATAM flight offers page in headless mode, waits for the page to load, and scrapes information about each flight.
2. **playwright_script.py**: Uses Playwright in headless mode to achieve the same objective, highlighting an alternative approach with a modern browser automation framework.

These scripts are ideal for demonstrations or quick scraping tasks where dynamic content rendering requires a browser interaction, such as JavaScript-rendered content.


## Prerequisites

- **Python 3.8+**
- **Google Chrome** (for `selenium_script.py`)
- **Node.js** (for Playwright)

## Installation

1. Clone the repository:
```bash
   git clone git@github.com:cbveritas/selenium_playwright.git
   cd selenium_playwright
```

2. Set up a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Install the Playwright browsers if not installed:
```bash
playwright install
```

4. How to Run
## Running the Selenium Script
```bash
python selenium_script.py
```

## Running the Playwright Script
```bash
python playwrigth_script.py
```
## Code Highlights
### Selenium Script
Configures Chrome to run headlessly, using webdriver-manager to simplify driver management.
Uses WebDriverWait with expected conditions to handle dynamic loading of elements.
Demonstrates error handling with try-except blocks for cases when elements may not load.

### Playwright Script
Uses Playwright's sync API for synchronous browser control.
Waits for the flight elements using wait_for_selector.
Demonstrates a streamlined approach with query_selector_all for element selection.


## Troubleshooting
- ChromeDriver errors (Selenium): Ensure Chrome is installed and compatible with the ChromeDriver version.
- Playwright errors: Ensure Node.js is installed, as Playwright may need it to install browsers.


## Dependencies
- selenium: For automating browser interactions.
- webdriver-manager: To manage browser drivers automatically.
- playwright: For streamlined browser automation.

