#Code works for people who are alive and are not billionares
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/search?q=")

search_items = ["Alexandra daddario", "David Dobrik", "Lebron James", "Steve Harvey", "Ryan Garcia", "Joe Rogan", "Dana white", "Conor Mcgregor"]
search = driver.find_element_by_name("q")

file = open('info2.csv', 'w', encoding = "utf-8")
writer = csv.writer(file)
writer.writerow(['Name', 'Born', 'Birth-place', 'age', 'height'])

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
    Born = section.find_element_by_class_name("Eq0J8").text.split('(')[0]
    Birth = targets[1].text.replace(',', '').split(')')[1]
    age = section.find_element_by_class_name("Eq0J8").text.split(' ')[4]
    height = targets[2].text.split(':')[1]

    # write to sheets
    writer.writerow([Name, Born, Birth, age, height])

    print(item + ":")
    print(Born)
    print(Birth)
    print(age)
    print(height)
    print('\n')

file.close()
time.sleep(1)
driver.quit()