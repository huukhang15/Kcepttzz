from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options đầy đủ
import time

# Đường dẫn đến Brave
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
TIKTOK_URL = "https://www.tiktok.com/"

def configure_selenium():
    """
    Cấu hình Selenium để điều khiển Brave qua cổng debug 9222.
    Returns:
        webdriver: Đối tượng driver đã được cấu hình.
    """
    try:
        # Thiết lập options cho Selenium
        options = Options()  # Sử dụng Options đã import
        options.binary_location = BRAVE_PATH
        options.add_argument("--mute-audio")  # Tắt âm thanh
        options.add_argument("--disable-sound")  # Tắt âm thanh bổ sung
        options.debugger_address = "127.0.0.1:9222"  # Kết nối đến cổng debug của Brave

        # Khởi tạo driver
        driver = webdriver.Chrome(options=options)
        print("Selenium đã được cấu hình thành công.")

        # Mở trang TikTok
        driver.get(TIKTOK_URL)
        time.sleep(2)  # Chờ trang tải hoàn tất
        print("Đã mở trang TikTok.")

        return driver

    except Exception as e:
        print(f"Lỗi khi cấu hình Selenium: {str(e)}")
        return None

# Gọi hàm để cấu hình Selenium
driver = configure_selenium()