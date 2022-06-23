from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
first_name = 'Gleb'
last_name = 'Kanafiev'
email = 'kanafiev@gamil.com'
current_dir = os.path.abspath(os.path.dirname(__file__))  # Получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'lesson2_2_step8_about_me.txt')  # Добваляем к этому пути имя файла

try:
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys(first_name)
    browser.find_element(By.NAME, 'lastname').send_keys(last_name)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(7)
    browser.quit()
