from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = "https://web.whatsapp.com/"
chrome_options = Options()
chrome_options.add_argument("user-data-dir=./.data/")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(web)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Recordatorios']"))).click()
message = input()
while message != "fin":
    driver.find_element(By.CSS_SELECTOR, "[title='Escribe un mensaje aquí']").send_keys(message)
    driver.find_element(By.CSS_SELECTOR, "[data-icon='send']").click()
    message = input()

time.sleep(1)
driver.close()