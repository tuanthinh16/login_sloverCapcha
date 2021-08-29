from selenium import webdriver
import time
import urllib
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from random import uniform, randint, choice
import os
import requests
import sys

# if not os.path.exists('Profile'):
#     os.makedirs('Profile')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1980x1080")
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(
    executable_path='chromedriver.exe', chrome_options=chrome_options)

driver.get('https://www.facebook.com/signup')
time.sleep(3)
# driver.find_element_by_xpath(
#     '//a [@role="button" and @class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
# time.sleep(3)
select = Select(driver.find_element_by_id('day'))
time.sleep(2)
select.select_by_visible_text('14')
time.sleep(2)
select = Select(driver.find_element_by_id('month'))
time.sleep(2)
select.select_by_value('12')
time.sleep(2)
select = Select(driver.find_element_by_id('year'))
time.sleep(2)
select.select_by_visible_text('2000')
time.sleep(2)


4 thg:
2 cơ đầu trường ăn: + 70K ( quân béo -20k quân hồ -30k thịnh - 20k)
cơ sau t ăn là + 30K(quân hồ -10 quân béo -10 trường thùy - 10)
3 thằng:
quân hồ 4 cơ là +80k ( t -40k trường -40k)
t ăn 2 cơ là +40( quân -20k trường -20k)

trường : +70 - 10 -40 - 20 = 0k.
quân hồ : +80 - 30 - 10 -20 : +20k
t : +30 +40 -20 -40: +10k.
quân béo : -20-10: -30k. đưa t 10k quân hồ 20k.
xong kèo

tiền giờ 170k :
quân béo -35k
trường - 45k
t -45k
tiền nước 30k quân trả 20k ( nước quân với quân béo) t -10k nước
 tổng cộng: 
quân béo -35k giờ -30k kèo đưa quân hồ
trường : -45k tiền giờ đưa quân hồ
t : -45k đưa quân 10k bên quân béo thua kèo bù qua nước
tổng quân nhận +65(quân béo) + 45k t + 45k trường : 155k (45k giờ m là 2l tròn)