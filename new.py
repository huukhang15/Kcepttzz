from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Đường dẫn tới Brave trên máy của bạn
brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Thay đổi theo đường dẫn của bạn

# Cấu hình tùy chọn
options = Options()
options.binary_location = brave_path  # Chỉ định Brave làm trình duyệt
options.add_argument("--incognito")   # Chạy ở chế độ ẩn danh

# Đường dẫn tới ChromeDriver
driver_path = "D:\chrome-win32\chrome-win32\chrome.exe"  # Thay đổi theo đường dẫn của bạn

# Khởi động trình duyệt
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Mở một trang web để kiểm tra
driver.get("https://www.google.com")

# Đóng trình duyệt sau khi xong (tùy chọn)
# driver.quit()