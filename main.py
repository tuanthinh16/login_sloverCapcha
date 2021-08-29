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


proxyList = '109.86.182.203:3128'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1980x1080")
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument(
    '--proxy-server=%s' % proxyList)
driver = webdriver.Chrome(
    executable_path='chromedriver.exe', chrome_options=chrome_options)
# driver.log(PROXY)
# chrome_options.capabilities['proxy'] = {
#     "proxyType": "MANUAL",
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY
# }
url = 'https://olacity.com/dashboard'
SpeechToTextURL = "https://speech-to-text-demo.ng.bluemix.net/"
username = 'tuanthinhdz@gmail.com'
password = 'concac11'
audioToTextDelay = 10
delayTime = 3
audioFile = "\\payload.mp3"


def delay():
    time.sleep(randint(2, 3))


def audioToText(audioFile):
    driver.execute_script('''window.open("","_blank")''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(SpeechToTextURL)

    delay()
    audioInput = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    audioInput.send_keys(audioFile)

    time.sleep(audioToTextDelay)

    text = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
    while text is None:
        text = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')

    result = text.text

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return result


def slover_cappcha():
    g_recaptcha = driver.find_elements_by_class_name('g-recaptcha')[0]
    outerIframe = g_recaptcha.find_element_by_tag_name('iframe')
    outerIframe.click()

    iframes = driver.find_elements_by_tag_name('iframe')
    audioBtnFound = False
    audioBtnIndex = -1

    for index in range(len(iframes)):
        driver.switch_to.default_content()
        iframe = driver.find_elements_by_tag_name('iframe')[index]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(delayTime)
        delay()
        try:
            audioBtn = driver.find_element_by_id("recaptcha-audio-button")
            if audioBtn:
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break
        except Exception as e:
            pass

    if audioBtnFound:
        try:
            while True:
                # get the mp3 audio file
                src = driver.find_element_by_id(
                    "audio-source").get_attribute("src")
                print("[INFO] Audio src: %s" % src)

                # download the mp3 audio file from the source
                urllib.request.urlretrieve(src, os.getcwd() + audioFile)

                # Speech To Text Conversion
                key = audioToText(os.getcwd() + audioFile)
                print("[INFO] Recaptcha Key: %s" % key)

                driver.switch_to.default_content()
                iframe = driver.find_elements_by_tag_name('iframe')[
                    audioBtnIndex]
                driver.switch_to.frame(iframe)

                # key in results and submit
                inputField = driver.find_element_by_id("audio-response")
                inputField.send_keys(key)
                delay()
                inputField.send_keys(Keys.ENTER)
                delay()

                err = driver.find_elements_by_class_name(
                    'rc-audiochallenge-error-message')[0]
                if err.text == "" or err.value_of_css_property('display') == 'none':
                    print("[INFO] Success!")
                    break

        except Exception as e:
            print(e)
            sys.exit(
                "[INFO] Possibly blocked by google. Change IP,Use Proxy method for requests")
    else:
        sys.exit("[INFO] Audio Play Button not found! In Very rare cases!")


# main
driver.get(url)
time.sleep(2)

driver.find_element_by_name('email').send_keys(username)
time.sleep(3)
driver.find_element_by_name('password').send_keys(password)
time.sleep(3)

slover_cappcha()
driver.find_elements_by_xpath(
    '//button [@type="submit" and @class="btn btn-main-primary btn-block"]').click()
driver.quit()
