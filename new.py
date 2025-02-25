import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
FOLLOWING_URL = "https://www.tiktok.com/following"
# Định nghĩa BRAVE_PATH ngay trong file này
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_URL = "https://www.tiktok.com/@{user}"

#======== Cấu hình brave =========#
def chay_brave():
    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)

# Chạy Brave lần đầu
time.sleep(1)  # Chờ một chút trước khi mở trình duyệt
chay_brave()

#========= Cấu hình Selenium =========#
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument("--mute-audio")
options.add_argument("--disable-sound")
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

# Mở trang TikTok
driver.get(TIKTOK_URL)