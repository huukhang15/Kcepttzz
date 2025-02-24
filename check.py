from pystyle import Write
import sys
import time

# Định nghĩa các màu ANSI
BLUE_LIGHT = '\033[38;5;159m'  # Xanh dương rất nhạt
BLUE_SOFT = '\033[38;5;123m'   # Xanh dương nhạt
BLUE_MEDIUM = '\033[38;5;75m'  # Xanh dương vừa
BLUE_STRONG = '\033[38;5;33m'  # Xanh dương đậm
BLUE_DARK = '\033[38;5;18m'   # Xanh dương đậm tối
RESET = '\033[0m'              # Reset màu về mặc định

# Danh sách dòng và màu
lines = [
    ("Dòng 1: Đây là xanh rất nhạt", BLUE_LIGHT),
    ("Dòng 2: Đây là xanh nhạt", BLUE_SOFT),
    ("Dòng 3: Đây là xanh vừa", BLUE_MEDIUM),
    ("Dòng 4: Đây là xanh đậm", BLUE_STRONG),
    ("Dòng 5: Đây là xanh đậm tối", BLUE_DARK),
]

# In từng dòng với hiệu ứng thủ công
for text, color in lines:
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.03)  # Tốc độ đánh máy
    print()  # Xuống dòng sau mỗi dòng