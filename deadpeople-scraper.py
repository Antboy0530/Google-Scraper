import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/search?q=")

search_items = ["muhammad ali", "Hitler", "stan lee", "George Washington", "Martin luther king", "Ghandi", "Albert Einstein"]
search = driver.find_element_by_name("q")

file = open('deadpeople.csv', 'w', encoding = "utf-8")
writer = csv.writer(file)
writer.writerow(['Name', 'Born', 'Birth-place', 'death', 'age'])

for item in search_items:
    search.clear()
    search.send_keys(item)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    url = driver.current_url
    driver.get(url)
    search = driver.find_element_by_name("q")
    info = driver.find_element_by_id("kp-wp-tab-overview")
    section = info.find_element_by_class_name("UDZeY") # remember when the class name has a space between them, it seperate names (dont put them together)
    targets = section.find_elements_by_class_name("wDYxhc") # list of each part of info section

    Name = item
    Born = section.find_element_by_class_name("Eq0J8").text.split(',')
    Born1 = Born[0] + "," + Born[1]
    Birth = section.find_element_by_class_name("Eq0J8").text.split(',')
    Birth1 = Birth[2] + "," + Birth[3]
    death = targets[2].find_element_by_class_name("Eq0J8").text.split(',')
    death1 = death[0] + ',' + death[1]
    age = int(death[1]) - int(Born[1])

    # write to sheets
    writer.writerow([Name, Born1, Birth1, death1, age])

    print(item + ":")
    print(Born1)
    print(Birth1)
    print(death1)
    print(age)
    print('\n')

file.close()
time.sleep(1)
driver.quit()