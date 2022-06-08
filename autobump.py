from selenium import webdriver
import chromedriver_binary
import time
from fake_useragent import UserAgent
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException


def bumping():
    delay = 10
    trades = int(input('How many trades you wanna bump?[1-15]: '))
    mail, password = 'username', 'password'
    ua = UserAgent()
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument(f"user-agent={ua.random}")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--log-level=1")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("disable-infobars")
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except WebDriverException:
            driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://rocket-league.com/login')
        driver.find_element(By.ID, 'acceptPrivacyPolicy').click()
        driver.find_element(By.NAME, 'email').send_keys(mail)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.NAME, 'submit').click()
        driver.get(driver.find_element(By.XPATH, '/html/body/header/section[1]/div/div[4]/div/a').get_attribute('href'))
        y = 1200
        for trade in range(1, trades + 1):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 480
            time.sleep(1)
            try:
                driver.find_element(By.XPATH, f'/html/body/main/section/div/div/div[3]/div/div[4]/div[{trade}]/div[2]/button').click()
            except ElementClickInterceptedException:
                pass
            try:
                WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/span/i')))
            except TimeoutException:
                time.sleep(delay)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/span/i').click()
            except ElementClickInterceptedException:
                pass
        driver.quit()
        time.sleep(random.randint(910, 1000))


def main():
    bumping()


if __name__ == '__main__':
    main()
