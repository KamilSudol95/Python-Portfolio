from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        cookies_btn = self.driver.find_element(By.CSS_SELECTOR, value='#onetrust-reject-all-handler')
        cookies_btn.click()
        time.sleep(1)
        go_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(55)
        x_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        x_btn.click()
        time.sleep(1)
        download_amount = int(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        upload_amount = int(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://x.com/login')
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_input.send_keys(f'{TWITTER_EMAIL}')

        dalej_btn = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        dalej_btn.click()
        time.sleep(2)

        password_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(f'{TWITTER_PASSWORD}')
        time.sleep(1)

        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_btn.click()
        time.sleep(5)

        tweet_layout = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f'Hello my dear ISP, why is my internet speed {self.down} down/{self.up} up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}UP?'
        tweet_layout.send_keys(tweet)
        time.sleep(3)

        tweet_btn = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_btn.click()
        time.sleep(3)

        self.driver.quit()


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'YOUR_EMAIL_ADDRESS'
TWITTER_PASSWORD = 'YOUR_X_PASSWORD'

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()