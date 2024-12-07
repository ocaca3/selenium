from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

#オプション設定
options = Options()
#ブラウザを開いたまま処理終了
options.add_experimental_option("detach", True)
# "Chromeは自動テストソフトウェアによって胃制御されています"を非表示にする
options.add_experimental_option('excludeSwitches', ['enable-automation'])
#パスワード保存ポップアップを無効化してブラウザ起動
prefs = {
    "credentials_enable_service": False
}
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(options=options)
#AWSコンソールサインイン画面を開く
browser.get("https://aws.amazon.com/jp/console/")
elem = browser.find_element(By.XPATH, '//*[@id="aws-page-content-main"]/div[2]/div/div/div[2]/div[2]/div/a')
elem.click()
time.sleep(10)
#ログイン実施
load_dotenv()
#Enter AccountID
elem = browser.find_element(By.XPATH , '//*[@id="account"]')
elem.send_keys(os.environ["USER_ACCOUNT"])
#Enter Username
elem = browser.find_element(By.XPATH, '//*[@id="username"]')
elem.send_keys(os.environ["USER_ID"])
#Enter Password
elem = browser.find_element(By.XPATH, '//*[@id="password"]')
elem.send_keys(os.environ["USER_PASSWORD"])
#Enter SingIn
elem = browser.find_element(By.XPATH, '//*[@id="signin_button"]')
elem.click()
#--------------MFAコードの入力,Submit--------------
input = input("MFAコードを入力してください。")
elem = browser.find_element(By.XPATH, '//*[@id="mfaCode"]')
elem.send_keys(input)
elem.send_keys(Keys.ENTER)
time.sleep(10)

#ap-northeast-1, S3で資料採取
browser.get('https://ap-northeast-1.console.aws.amazon.com/s3/home?region=ap-northeast-1#')
elem = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/div/nav/div[2]/div/ul[1]/li[1]/a/span')
elem.click()