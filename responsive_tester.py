import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("http://thdnice.tistory.com")
browser.maximize_window()

sizes = [320, 480, 960, 1366, 1920]

print(browser.get_window_size())

for size in sizes:
    print(size)
    browser.set_window_size(size, 1000)
    time.sleep(1)
    # by using return, we can get return value from java script
    scroll_size = browser.execute_script("return document.body.scrollHeight")
    print(scroll_size)
    time.sleep(5)
