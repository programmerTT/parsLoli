from selenium import webdriver
import pickle
data = ['FirstAkk','SecondAkk']
options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled',False)
driver = webdriver.Firefox(options=options)
driver.get('https://loliland.ru/ru/login?return_to=/ru/cabinet/bonus')
def click(akk):
    cookies = pickle.load(open(f'{akk}.pkl','rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.find_element('css selector','button.button-p').click()
    driver.get('https://loliland.ru/ru/cabinet/authorization')
    driver.find_element('css selector','button-s_size_small').click()
click('FirstAkk')
'''for i in range(len(data)):
    try: click(data[i])
    except:pass'''
