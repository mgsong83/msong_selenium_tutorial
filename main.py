from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


chrome_opt = Options()
chrome_opt.add_experimental_option("detach", True)
chrome_opt.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_opt)
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
search_bar.send_keys("rtx3070")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")
print(search_results)


for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)
