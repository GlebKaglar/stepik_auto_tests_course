import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    answer = calc(browser.find_element(By.ID, 'input_value').text)

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'robotCheckbox').click()

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")  # Присваиваем значение атрибута
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    browser.quit()
