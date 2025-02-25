import time
import os
import subprocess
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

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

            return {
                'success': True,
                'username': username,
                'nickname': nickname,
                'follower_count': followers_count.group(1) if followers_count else 'N/A',
                'following_count': following_count.group(1) if following_count else 'N/A'
            }
        return {'success': False, 'message': 'Cookie không hợp lệ hoặc đã hết hạn'}

#========= Khởi chạy Brave (Incognito Mode) =========#
def chay_brave():
    try:
        subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
        time.sleep(3)
    except Exception as e:
        print(f"Lỗi khi khởi chạy Brave: {str(e)}")

#========= Cấu hình Selenium =========#
def setup_driver():
    try:
        options = Options()
        options.binary_location = BRAVE_PATH
        options.add_argument("--mute-audio")
        options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"Lỗi khi khởi tạo driver: {str(e)}")
        return None

#========= Xử lý cookie =========#
def dang_nhap_tiktok():
    cookie_file = 'cookietiktok.txt'
    cookie_final = ''

    if not os.path.exists(cookie_file):
        with open(cookie_file, 'w', encoding='utf-8') as f:
            f.write('')

    with open(cookie_file, 'r', encoding='utf-8') as f:
        cookie_cu = f.read().strip()

    if cookie_cu:
        while True:
            su_dung_cu = input("Bạn muốn sử dụng cookie cũ không (Y/N): ").strip().upper()
            if su_dung_cu == 'Y':
                print("Sử dụng cookie cũ thành công.")
                cookie_final = cookie_cu
                break
            elif su_dung_cu == 'N':
                cookie_final = input("Nhập cookie mới của bạn: ").strip()
                if "=" not in cookie_final:
                    print("Cookie không tồn tại hoặc hết hạn")
                    continue
                with open(cookie_file, 'w', encoding='utf-8') as f:
                    f.write(cookie_final)
                print("Cookie mới đã được lưu.")
                break
            else:
                print("Vui lòng nhập đúng lựa chọn!")
    else:
        while True:
            cookie_final = input("Nhập cookie mới của bạn: ").strip()
            if "=" not in cookie_final:
                print("Cookie không tồn tại hoặc hết hạn")
                continue
            with open(cookie_file, 'w', encoding='utf-8') as f:
                f.write(cookie_final)
            print("Cookie mới đã được lưu.")
            break

    cookies = [c.strip() for c in cookie_final.split(';') if "=" in c]
    return cookies if cookies else []

if __name__ == "__main__":
    chay_brave()
    driver = setup_driver()
    if driver:
        cookies = dang_nhap_tiktok()
        if cookies:
            cookie_final = '; '.join(cookies)
            tiktok_login = TikTokLogin()
            result = tiktok_login.login_with_cookie(cookie_final)
            if result['success']:
                print(f"\n===== Đăng nhập thành công! =====")
                print(f"Username: {result['username']}")
                print(f"Link tài khoản: https://www.tiktok.com/@{result['username']}")
                print(f"Số người theo dõi: {result['follower_count']}")
                print(f"Số người đang theo dõi: {result['following_count']}")
            else:
                print(result['message'])
