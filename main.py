from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    #browser.implicitly_wait(5)
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    button = browser.find_element(By.ID, "answer")
    button.send_keys(y)
    sub2 = browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(15)
    browser.quit()


