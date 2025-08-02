from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://react.dev"

    def open(self):
        """Navigate to the homepage URL."""
        self.driver.get(self.url)

    def get_header(self):
        """Return the header element if present, else None."""
        try:
            return self.driver.find_element(By.TAG_NAME, "header")
        except:
            return None

    def get_footer(self):
        """Return the footer element if present, else None."""
        try:
            return self.driver.find_element(By.TAG_NAME, "footer")
        except:
            return None

    def get_navbar(self):
        """Return the navigation bar element if present, else None."""
        try:
            return self.driver.find_element(By.TAG_NAME, "nav")
        except:
            return None

    def get_nav_link(self, text):
        """Return a navigation link element by its visible text."""
        return self.driver.find_element(By.LINK_TEXT, text)

    def get_theme_toggle(self):
        """Return the theme toggle button (dark mode)."""
        return self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Use Dark Mode"]')

    def get_html_theme(self):
        """Return the class attribute of the <html> element (theme info)."""
        return self.driver.find_element(By.TAG_NAME, "html").get_attribute("class")

    def get_search_trigger(self):
        """Return the search bar trigger button."""
        return self.driver.find_element(By.XPATH, '//button[contains(., "Search")]')

    def open_search_bar(self):
        """
        Open the search bar if it's not already open.
        Waits for the trigger to be clickable and the input to be visible.
        """
        if self.driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Search docs"]'):
            return

        trigger = self.get_search_trigger()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trigger)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Search")]'))
        )
        trigger.click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search docs"]'))
        )

    def search_and_click_first_result(self, query):
        """
        Enter a search query and click the first result.
        Waits for the input and result to be interactable.
        """
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search docs"]'))
        )
        input_box.clear()
        input_box.send_keys(query)

        first_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.DocSearch-Hit a'))
        )
        first_result.click()

    def save_most_recent_result(self):
        """
        Click the 'star' button to save the most recent search result.
        """
        star_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.DocSearch-Hit-action-button'))
        )
        star_button.click()

    def get_favorite_search_titles(self):
        """
        Return a list of titles from the current search results.
        """
        self.open_search_bar()
        titles = self.driver.find_elements(By.CSS_SELECTOR, 'span.DocSearch-Hit-title')
        return [title.text for title in titles]

    def click_translation_button(self):
        """
        Click the translations button in the UI.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Translations"]'))
        )
        button.click()

    def click_translation_link_by_text(self, language_text):
        """
        Click a translation link by partial language text.
        """
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, language_text))
        )
        link.click()

    def click_translation_and_switch_to_new_tab(self, language_text):
        """
        Click a translation link and switch to the newly opened tab.
        Returns the handle of the original tab.
        """
        main_tab = self.driver.current_window_handle

        self.click_translation_link_by_text(language_text)

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_tab = [tab for tab in self.driver.window_handles if tab != main_tab][0]

        self.driver.switch_to.window(new_tab)
        return main_tab

    def verify_current_url_contains(self, expected_url):
        """
        Wait until the current URL contains the expected substring.
        Returns True if found.
        """
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))
        return expected_url in self.driver.current_url

    def close_current_tab_and_switch_back(self, main_tab):
        """
        Close the current browser tab and switch back to the main tab.
        """
        self.driver.close()
        self.driver.switch_to.window(main_tab)



