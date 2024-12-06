from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


region_list = {'ap-northeast-1': 'https://ap-northeast-1.console.aws.amazon.com/console/home?region=ap-northeast-1#',
               'ap-northeast-3': 'https://ap-northeast-3.console.aws.amazon.com/console/home?region=ap-northeast-3#',
               'us-east-1': 'https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1#'
               }

browser = webdriver.Chrome()
#AWSコンソールサインイン画面を開く
browser.get("https://aws.amazon.com/jp/console/")
elem = browser.find_element(By.XPATH, '//*[@id="aws-page-content-main"]/div[2]/div/div/div[2]/div[2]/div/a')
#ログイン実施
load_dotenv()
#Enter AccountID
elem = browser.find_element(By.XPATH, '//*[@id="account"]')
elem.send_keys(os.environ["USER_ID"])
#Enter Username
elem = browser.find_element(By.XPATH, '//*[@id="username"]')
elem.send_keys('abcdefghijklmnopqrstu')
#Enter Password
elem = browser.find_element(By.XPATH, '//*[@id="password"]')
elem.send_keys('password')


# #ap-northeast-1, S3で資料採取
# browser.get('https://ap-northeast-1.console.aws.amazon.com/s3/home?region=ap-northeast-1#')
# elem = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/div/nav/div[2]/div/ul[1]/li[1]/a/span')
# elem.click()