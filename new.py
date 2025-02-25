import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

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

#========= Đăng nhập TikTok bằng Cookie =========#
def dang_nhap_tiktok(driver):
    cookie_final = input("Nhập cookie TikTok của bạn: ").strip()

    driver.get(TIKTOK_URL)
    cookies = [c.strip() for c in cookie_final.split(';') if '=' in c]
    for cookie in cookies:
        name, value = cookie.split('=', 1)
        driver.add_cookie({'name': name.strip(), 'value': value.strip(), 'domain': '.tiktok.com'})
    driver.refresh()

if __name__ == "__main__":
    chay_brave()
    driver = setup_driver()
    if driver:
        dang_nhap_tiktok(driver)
        print("Đăng nhập thành công bằng cookie!")
