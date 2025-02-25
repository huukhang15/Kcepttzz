import subprocess
import time

# Đường dẫn đến Brave
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

def start_brave():
    """
    Khởi chạy Brave ở chế độ ẩn danh với cổng debug 9222.
    Đóng các phiên Brave hiện có trước khi mở mới để tránh xung đột.
    """
    try:
        # Đóng các tiến trình Brave đang chạy (nếu có)
        subprocess.call("taskkill /IM brave.exe /F", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Mở Brave với chế độ debug
        subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
        # Chờ 5 giây để đảm bảo Brave khởi động xong
        time.sleep(5)
        print("Brave đã được khởi động ở chế độ debug trên cổng 9222.")
    except Exception as e:
        print(f"Lỗi khi khởi động Brave: {str(e)}")

# Gọi hàm để khởi động Brave
start_brave()