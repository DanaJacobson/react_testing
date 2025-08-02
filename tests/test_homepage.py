import time
from pages.homepage import HomePage

def test_header_exists(driver):
    homepage = HomePage(driver)
    homepage.open()
    header = homepage.get_header()
    assert header is not None, "Header not found on the page"

def test_footer_exists(driver):
    homepage = HomePage(driver)
    homepage.open()
    footer = homepage.get_footer()
    assert footer is not None, "Footer not found on the page"

def test_navbar_exists(driver):
    homepage = HomePage(driver)
    homepage.open()
    assert homepage.get_navbar() is not None, "Navbar not found on the page"

def test_nav_links_work(driver):
    homepage = HomePage(driver)
    homepage.open()

    links = {
        "Learn": "https://react.dev/learn",
        "Reference": "https://react.dev/reference/react",
        "Community": "https://react.dev/community",
        "Blog": "https://react.dev/blog"
    }

    for text, expected_url in links.items():
        link = homepage.get_nav_link(text)
        link.click()
        time.sleep(1)
        assert driver.current_url.startswith(expected_url), f"Expected URL to start with {expected_url}, but got {driver.current_url}"
        homepage.open()

def test_theme_toggle(driver):
    homepage = HomePage(driver)
    homepage.open()

    original_theme = homepage.get_html_theme()
    toggle = homepage.get_theme_toggle()
    toggle.click()
    time.sleep(2)
    new_theme = homepage.get_html_theme()

    assert new_theme != original_theme, "Theme class did not change after clicking toggle"

def test_search_functionality(driver):
    homepage = HomePage(driver)
    homepage.open()

    query = "custom hook"

    homepage.open_search_bar()
    homepage.search_and_click_first_result(query)
    time.sleep(2)
    homepage.open_search_bar()
    homepage.save_most_recent_result()
    time.sleep(2)
    titles = homepage.get_favorite_search_titles()
    assert any("custom hook" in title.lower() for title in titles), "Search was not saved to favorites"

def test_translation_links(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_translation_button()

    translations = {
        "English": "https://react.dev/",
        "French": "https://fr.react.dev/",
        "Chinese": "https://zh-hans.react.dev/",
        "Spanish": "https://es.react.dev/"
    }

    for language, expected_url in translations.items():
        main_tab = homepage.click_translation_and_switch_to_new_tab(language)
        assert homepage.verify_current_url_contains(expected_url), f"URL does not contain expected language path: {expected_url}"
        homepage.close_current_tab_and_switch_back(main_tab)
