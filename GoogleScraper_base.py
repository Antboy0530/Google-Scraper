from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/search?q=")

search_items = ["Olympics", "China", "United States", "Peru", "Mexico", "Canada"]
search = driver.find_element_by_name("q")
# search.clear()
# search.send_keys("Pokemon")
# search.send_keys(Keys.RETURN)

# note: seems like the div id of info section on the right remains the same after each search id = "kp-wp-tab-overview"
for item in search_items:
    search.clear()
    search.send_keys(item)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    url = driver.current_url
    driver.get(url)
    search = driver.find_element_by_name("q")
    info = driver.find_element_by_id("kp-wp-tab-overview")
    specify = info.find_element_by_tag_name("div") # grabs first div inside info

    print(item + ":")
    print(specify.text + "\n")


time.sleep(1)
driver.quit()