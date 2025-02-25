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
driver = webdriver.Chrome(options=options)
driver.get(TIKTOK_URL)
#=====Đăng nhập bằng cookie====
def dang_nhap_tiktok():
    """
    Hàm xử lý đăng nhập TikTok bằng cookie.
    Returns:
        list: Danh sách các cookie đã được xử lý
    """
    os.system('cls')
    try:
        cookie_file = 'cookietiktok.txt'
        cookie_final = ''
        
        # Kiểm tra và tạo file cookie nếu chưa tồn tại
        if not os.path.exists(cookie_file):
            with open(cookie_file, 'w', encoding='utf-8') as f:
                f.write('')
        
        # Đọc cookie cũ từ file
        with open(cookie_file, 'r', encoding='utf-8') as f:
            cookie_cu = f.read().strip()
        
        # Xử lý trường hợp có cookie cũ
        if cookie_cu:
            while True:
                su_dung_cu = input(f"{trang}Bạn muốn sử dụng cookie cũ không (Y/N): ").strip().upper()
                if su_dung_cu == 'Y':
                    for _ in range(15): print(f"{xl}Sử dụng cookie cũ thành công.", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
                    cookie_final = cookie_cu
                    break
                elif su_dung_cu == 'N':
                    # Nhập và lưu cookie mới
                    cookie_final = input(f"{trang}Nhập cookie mới của bạn: ").strip()
                    if "=" not in cookie_final:
                        for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
                        continue
                    with open(cookie_file, 'w', encoding='utf-8') as f:
                        f.write(cookie_final)
                        for _ in range(15): print(f"{xl}Cookie mới đã được lưu.", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
                    break
                else:
                    print("\033[F\033[K", end="")  # Xóa thông báo lỗi
                    for _ in range(5): print(f"{red}Vui lòng nhập đúng lựa chọn!", end="\r", flush=True); time.sleep(0.2); print(" " * 30, end="\r", flush=True); time.sleep(0.2)
            print(" " * 50, end="\r")  # Xóa lỗi khỏi màn hình
        else:
            # Nhập và lưu cookie mới nếu không có cookie cũ
            while True:
                cookie_final = input(f"{trang}Nhập cookie mới của bạn: ").strip()
                if "=" not in cookie_final:
                    for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
                    continue
                with open(cookie_file, 'w', encoding='utf-8') as f:
                    f.write(cookie_final)
                    for _ in range(15): print(f"{xl}Cookie mới đã được lưu.", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
                break
        
        # Xử lý cookie thành list
        cookies = [c.strip() for c in cookie_final.split(';') if "=" in c]
        if not cookies:
            for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn", end="\r"); time.sleep(0.2); print(" " * 30, end="\r"); time.sleep(0.2)
            return []
            
        return cookies
        
    except Exception as e:
        print(f"Lỗi khi xử lý cookie: {str(e)}")
        return []






#========= Đăng nhập bằng Cookie (Requests) =========#
class TikTokLogin:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "referer": "https://www.tiktok.com/",
            "authority": "www.tiktok.com"
        }

    def login_with_cookie(self, cookies_str):
        for cookie in cookies_str.split(';'):
            if '=' in cookie:
                name, value = cookie.split('=', 1)
                self.session.cookies.set(name.strip(), value.strip(), domain='.tiktok.com')

        response = self.session.get("https://www.tiktok.com/passport/web/account/info/", headers=self.headers)
        
        if response.status_code == 200:
            data = response.json().get('data', {})
            username = data.get('username', 'N/A')
            nickname = data.get('nickname', 'N/A')
            profile_url = f"https://www.tiktok.com/@{username}"

            profile_response = self.session.get(profile_url, headers=self.headers)
            followers_count = re.search(r'"followerCount":(\d+)', profile_response.text)
            following_count = re.search(r'"followingCount":(\d+)', profile_response.text)
            print(f"\n{luc}===== Đăng nhập thành công! =====")
            print(f"{trang}Username: {result['username']}")
            print(f"{trang}Link tài khoản: https://www.tiktok.com/@{result['username']}")
            print(f"{trang}Số người theo dõi: {result['follower_count']}")
            print(f"{trang}Số người đang theo dõi: {result['following_count']}")
            print(f"={xl}" * 50)
            return {
                'success': True,
                'username': username,
                'nickname': nickname,
                'follower_count': followers_count.group(1) if followers_count else 'N/A',
                'following_count': following_count.group(1) if following_count else 'N/A'
            }
        return {'success': False, 'message': 'Cookie không hợp lệ hoặc đã hết hạn'}