from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(3)
    print(browser.switch_to.alert.text.split(" ")[-1])
    browser.quit()
