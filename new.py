import requests
import time
import subprocess
import random
import re
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pystyle import Write, Colors
import subprocess, sys; [subprocess.check_call([sys.executable, "-m", "pip", "install", lib]) for lib in ["requests", "selenium", "pystyle"] if __import__(lib, globals(), locals(), [], 0) is None]
from datetime import datetime
import time

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
FOLLOWING_URL = "https://www.tiktok.com/following"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_URL = "https://www.tiktok.com/@{user}"
#============Brave&senlium================
def chay_brave():
    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
    time.sleep(1)  # Chờ một chút trước khi mở trình duyệt

chay_brave()

#========= Cấu hình Selenium =========#
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument("--mute-audio")
options.add_argument("--disable-sound")
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

#========= Đăng nhập Cookie vào Brave (Selenium) =========#
driver.get(TIKTOK_URL)  # Cần mở trang trước khi thêm cookie