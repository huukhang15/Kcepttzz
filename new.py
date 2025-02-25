import subprocess
import time
import selenium  # Import module chính để kiểm tra
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options rõ ràng

# Đường dẫn đến Brave
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
TIKTOK_URL = "https://www.tiktok.com/"

def start_brave():
    """
    Khởi chạy Brave ở chế độ ẩn danh với cổng debug 9222.
    """
    try:
        subprocess.call("taskkill /IM brave.exe /F", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
        time.sleep(5)
        print("Brave đã được khởi động ở chế độ debug trên cổng 9222.")
    except Exception as e:
        print(f"Lỗi khi khởi động Brave: {str(e)}")

def configure_selenium():
    """
    Cấu hình Selenium để điều khiển Brave qua cổng debug 9222.
    Returns:
        webdriver: Đối tượng driver đã được cấu hình.
    """
    try:
        # Kiểm tra xem Options có được import không
        print("Kiểm tra: Options đã được import từ selenium.webdriver.chrome.options")
        options = Options()  # Nếu lỗi xảy ra ở đây, vấn đề là do import
        options.binary_location = BRAVE_PATH
        options.add_argument("--mute-audio")
        options.add_argument("--disable-sound")
        options.debugger_address = "127.0.0.1:9222"
        
        driver = webdriver.Chrome(options=options)
        print("Selenium đã được cấu hình thành công.")
        driver.get(TIKTOK_URL)
        time.sleep(2)
        print("Đã mở trang TikTok.")
        return driver
    except Exception as e:
        print(f"Lỗi khi cấu hình Selenium: {str(e)}")
        return None

# Thực thi
start_brave()
driver = configure_selenium()