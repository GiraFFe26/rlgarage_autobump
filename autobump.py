from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException


def bumping():
    delay = 10
    trades = int(input('How many trades you wanna bump?[1-15]: '))
    mail, password = 'mail', 'password'
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    s = Service(executable_path='./chromedriver.exe')
    while True:
        try:
            driver = webdriver.Chrome(service=s, options=options)
        except WebDriverException:
            driver = webdriver.Chrome(service=s, options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
          '''
        })
        driver.get('https://rocket-league.com/login')
        try:
            WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, 'acceptPrivacyPolicy')))
        except TimeoutException:
            time.sleep(delay)
        driver.find_element(By.ID, 'acceptPrivacyPolicy').click()
        driver.find_element(By.NAME, 'email').send_keys(mail)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.NAME, 'submit').click()
        try:
            WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, '/html/body/header/section'
                                                                                         '[1]/div/div[4]/div/a')))
        except TimeoutException:
            time.sleep(delay)
        driver.get(driver.find_element(By.XPATH, '/html/body/header/section[1]'
                                                 '/div/div[4]/div/div/ul/li[2]/a').get_attribute('href'))
        y = 1200
        for trade in range(1, trades + 1):
            driver.execute_script(f"window.scrollTo(0,{y})")
            y += 480
            time.sleep(1.5)
            try:
                driver.find_element(By.XPATH, f'/html/body/main/section/div/div[3]/div[2]/'
                                              f'div/div[4]/div[{trade}]/div[2]/button').click()
            except ElementClickInterceptedException:
                pass
            try:
                WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, '/html/body'
                                                                                             '/div[2]/div/span/i')))
            except TimeoutException:
                time.sleep(delay)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/span/i').click()
            except ElementClickInterceptedException:
                pass
        driver.quit()
        time.sleep(880)


def main():
    bumping()


if __name__ == '__main__':
    main()
