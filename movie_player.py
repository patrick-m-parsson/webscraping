from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

service = Service("c:\\project\\chromedriver.exe")
option = Options()
option.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=service, options=option)
driver.get('https://www.youtube.com/watch?v=DXUAyRRkI6k')

# wait for the page to load everything (works without it)
for i in range(10):
    print(i)
    time.sleep(1)

video = driver.find_element(By.CLASS_NAME, 'ytp-play-button')
#video.send_keys(Keys.SPACE) #hits space
video.click()  

time.sleep(10)
driver.quit()