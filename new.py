import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
FOLLOWING_URL = "https://www.tiktok.com/following"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_URL = "https://www.tiktok.com/@{user}"
#========= Cấu hình Selenium =========#
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument("--mute-audio")
options.add_argument("--disable-sound")
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#======== Cấu hình brave =========#
def chay_brave():
    subprocess.call("taskkill /IM brave.exe /F", shell=True)
    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
    time.sleep(5)

# Chạy Brave
chay_brave()



# Mở trang TikTok
driver.get(TIKTOK_URL)