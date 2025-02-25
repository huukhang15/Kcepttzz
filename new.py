import requests
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

#========= Khởi chạy Brave (Debug Mode) =========#
def chay_brave():
    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)

# Chờ một chút trước khi mở trình duyệt
time.sleep(1)
chay_brave()

#========= Cấu hình Selenium =========#
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument("--mute-audio")
options.add_argument("--disable-sound")
options.debugger_address = "127.0.0.1:9222"

# Mở trình duyệt
try:
    driver = webdriver.Chrome(options=options)
    driver.get(TIKTOK_URL)
    print("Đã mở TikTok thành công!")
except Exception as e:
    print(f"Lỗi khi mở trình duyệt: {e}")
