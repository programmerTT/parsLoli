from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pickle

data = {
                'login': f"RGB_Printer",
                'password': f"Mlpnko12"
            }
options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled',False)
driver = webdriver.Firefox(options=options)
driver.get('https://loliland.ru/ru/login?return_to=/ru/cabinet/bonus')
wait = WebDriverWait(driver,9999999)
wait.until(ec.title_contains('Бонусы - LoliLand'))

with open('SecondAkk.pkl','wb') as f:
    pickle.dump(driver.get_cookies(), f)


