from weakref import WeakKeyDictionary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GoogleKeywordScreenShoter:

    def __init__(self, Keyword, screen_dir):
        chrome_opt = Options()
# to stay browser open when code ends (need to quit() or close() to close browser)
        chrome_opt.add_experimental_option("detach", True)
# to remove bluetooth related error (don't know why)
        chrome_opt.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_opt)  # use chrome
        self.keyword = Keyword
        self.screendir = screen_dir

    def start(self):
        self.browser.get("https://google.com")

        search_bar = self.browser.find_element_by_class_name(
            "gLFyf")  # search bar class name (get from inspect)
        search_bar.send_keys(self.keyword)  # key word
        search_bar.send_keys(Keys.ENTER)

        try:
            shitty_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "qGXjvb")))  # wait until AD load

            # use JS code in python
            self.browser.execute_script(
                """
                const elements_to_remove = arguments[0];
                elements_to_remove.parentElement.removeChild(elements_to_remove);
                """,
                shitty_element
            )  # remove AD contents

        except Exception:
            pass

        search_results = self.browser.find_elements_by_class_name("g")
        print(search_results)

        for index, search_result in enumerate(search_results):
            title = search_result.find_element_by_tag_name("h3")
            if title:
                print(title.text)
            search_result.screenshot(
                f"{self.screendir}/{self.keyword}_{index}.png")

    def finish(self):
        self.browser.quit()


rtx3070 = GoogleKeywordScreenShoter("RTX3070", "screenshot")
rtx3070.start()
