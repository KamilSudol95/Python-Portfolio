from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.instagram.com/'
EMAIL = 'YOUR_EMAIL_ADDRESS' #Please store variable in virtual environment
PASSWORD = 'YOUR_PASSWORD' #Please store variable in virtual environment


similar_account = 'maxverstappen1'
followers_number = 5


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(URL)
        time.sleep(2)

        cookies_btn = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies_btn.click()

        email_btn = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_btn.send_keys(f'{EMAIL}')

        password_btn = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_btn.send_keys(f'{PASSWORD}')

        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        time.sleep(2)

        followers = self.driver.find_element(By.CSS_SELECTOR, value="ul li div a[href='/chefsteps/followers/']")
        followers.click()
        time.sleep(2)

        modal = self.driver.find_element(By.CSS_SELECTOR, value=".xyi19xy")
        for i in range (followers_number):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)



    def follow(self):
        all_btns = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for btn in all_btns:
            try:
                btn.click()
                time.sleep(1.25)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_btn.click()

bot = InstaFollower()
bot.login()
bot.find_followers()