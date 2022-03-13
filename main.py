from weakref import WeakKeyDictionary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


KEYWORD = "RTX 3080"

chrome_opt = Options()
# to stay browser open when code ends (need to quit() or close() to close browser)
chrome_opt.add_experimental_option("detach", True)
# to remove bluetooth related error (don't know why)
chrome_opt.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(ChromeDriverManager(
).install(), options=chrome_opt)  # use chrome
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name(
    "gLFyf")  # search bar class name (get from inspect)
search_bar.send_keys(KEYWORD)  # key word
search_bar.send_keys(Keys.ENTER)

shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "qGXjvb")))  # wait until AD load

# use JS code in python
browser.execute_script(
    """
    const elements_to_remove = arguments[0];
    elements_to_remove.parentElement.removeChild(elements_to_remove);
    """,
    shitty_element
)  # remove AD contents


search_results = browser.find_elements_by_class_name("g")
print(search_results)

for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)
