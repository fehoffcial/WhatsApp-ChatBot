import pyqrcode
import png
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()
options.headless = True
twms = webdriver.Chrome(options=options)
twms = Chrome()
twms.get("https://web.whatsapp.com/")
sleep(10)
try: ## Create a QR-CODE for acess for WhatsApp
    while True:
        qr_code_refresh = twms.find_element_by_css_selector("[class=_3l6Cf]").click()
        qr_code = twms.find_element_by_css_selector("[class=_1yHR2]").get_attribute("data-ref")
        qrcode = pyqrcode.create(qr_code)
        qrcode.png('code.png', scale=6)
        sleep(20)
except:
    twms.find_element_by_css_selector("._3Pwfx").click()
    twms.find_elements_by_css_selector("._1awRl.copyable-text.selectable-text")[-1].send_keys("OIE")
