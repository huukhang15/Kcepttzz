import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
driver = webdriver.Chrome(options=options)
#======== Cấu hình brave =========#
def chay_brave():
    # Đóng các phiên Brave đang chạy (nếu có)
    subprocess.call("taskkill /IM brave.exe /F", shell=True)
    # Mở Brave với chế độ debug
    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
    # Chờ lâu hơn để đảm bảo Brave khởi động
    time.sleep(5)

# Chạy Brave
chay_brave()



# Mở trang TikTok
driver.get(TIKTOK_URL)