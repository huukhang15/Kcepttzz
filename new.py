import requests
import time
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import re

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

#========= Khởi chạy Brave (Debug Mode) =========#
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
        options.add_argument("--disable-sound")
        options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=options)
        return driver
    except WebDriverException as e:
        print(f"Lỗi khi khởi tạo driver: {str(e)}")
        return None

#========= Đăng nhập TikTok bằng Cookie =========#
def dang_nhap_tiktok(driver):
    cookie_file = 'cookietiktok.txt'

    if not os.path.exists(cookie_file):
        with open(cookie_file, 'w', encoding='utf-8') as f:
            f.write('')

    with open(cookie_file, 'r', encoding='utf-8') as f:
        cookie_cu = f.read().strip()

    if cookie_cu:
        su_dung_cu = input("Bạn muốn sử dụng cookie cũ không (Y/N): ").strip().upper()
        if su_dung_cu == 'Y':
            cookie_final = cookie_cu
        else:
            cookie_final = input("Nhập cookie mới của bạn: ").strip()
            with open(cookie_file, 'w', encoding='utf-8') as f:
                f.write(cookie_final)
    else:
        cookie_final = input("Nhập cookie mới của bạn: ").strip()
        with open(cookie_file, 'w', encoding='utf-8') as f:
            f.write(cookie_final)

    driver.get(TIKTOK_URL)
    cookies = [c.strip() for c in cookie_final.split(';') if '=' in c]
    for cookie in cookies:
        name, value = cookie.split('=', 1)
        driver.add_cookie({'name': name.strip(), 'value': value.strip(), 'domain': '.tiktok.com'})
    driver.refresh()

#========= Lấy thông tin tài khoản =========#
def lay_thong_tin_tiktok(cookie_final):
    session = requests.Session()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "referer": "https://www.tiktok.com/",
        "authority": "www.tiktok.com"
    }

    for cookie in cookie_final.split(';'):
        if '=' in cookie:
            name, value = cookie.split('=', 1)
            session.cookies.set(name.strip(), value.strip(), domain='.tiktok.com')

    response = session.get("https://www.tiktok.com/passport/web/account/info/", headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', {})
        username = data.get('username', 'N/A')
        nickname = data.get('nickname', 'N/A')

        profile_url = f"https://www.tiktok.com/@{username}"
        profile_response = session.get(profile_url, headers=headers)
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

if __name__ == "__main__":
    chay_brave()
    driver = setup_driver()
    if driver:
        dang_nhap_tiktok(driver)

        with open('cookietiktok.txt', 'r', encoding='utf-8') as f:
            cookie_final = f.read().strip()

        result = lay_thong_tin_tiktok(cookie_final)
        if result['success']:
            print("===== Đăng nhập thành công! =====")
            print(f"Username: {result['username']}")
            print(f"Link tài khoản: https://www.tiktok.com/@{result['username']}")
            print(f"Số người theo dõi: {result['follower_count']}")
            print(f"Số người đang theo dõi: {result['following_count']}")
        else:
            print(f"Lỗi: {result['message']}")
