# React Documentation UI Testing

This project provides automated UI tests for the [React documentation website](https://react.dev) using Selenium WebDriver and Python.

## Project Structure

```
react_testing/
│
├── pages/
│   └── homepage.py         # Page Object Model for React homepage
│
├── tests/
│   └── test_homepage.py    # Automated UI tests for the homepage
│
├── utils/
│   └── driver_setup.py     # WebDriver setup utilities
│
├── conftest.py             # Pytest fixtures/configuration
├── requirements.txt        # Python dependencies
├── README.md
└── venv/                   # Optional - python virtual enviroment
```

## Tests Overview (`tests/test_homepage.py`)

The `test_homepage.py` file contains tests that:

- **Verify the presence of key UI elements:**  
  Checks for header, footer, and navigation bar on the homepage.
- **Test navigation links:**  
  Ensures navigation links are present and clickable.
- **Test theme toggle:**  
  Switches between light and dark mode and verifies the change.
- **Test search functionality:**  
  Opens the search bar, enters a query, and clicks the first result.
- **Test saving search results:**  
  Clicks the star button to save a search result.
- **Test translation links:**  
  Clicks the translation button, selects a language, and verifies the new tab opens with the correct URL.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd react_testing
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download WebDriver:**

   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
   - Make sure the WebDriver executable is in your system PATH.

## Running the Tests

From the root directory, run:

```bash
pytest tests/test_homepage.py
```

Or to run all tests in the `tests/` folder:

```bash
pytest
```

## Notes

- Ensure your WebDriver version matches your browser version.
- Adjust timeouts in the code if you experience flaky tests due to network speed.
- For visuals of the test runs: Comment out or remove the headless mode option in the  driver_setup to see the browser UI during test execution.