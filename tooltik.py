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
Defaut="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue      # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"
xduong = '\033[1;94m'
do2 = '\033[1;91m'
tim2 = '\033[0;95m'
xl = '\033[1;32m'
yellow3 = '\033[1;93m'
den = '\033[1;47;30m'
xn2 = '\033[1;96m'
do = '\033[1;31m'
hong = '\033[1;35m'
luc = '\033[1;92m'
trang = '\033[1;97m'
tim = '\033[0;35m'
yellow2 = '\033[1;33m'
gray = '\033[0;90m'
bblack = '\033[1;30m',
bred = '\033[1;31m',
bgreen = '\033[1;32m',
byelloww = '\033[1;33m',
bblue = '\033[1;34m',
bpurple = '\033[1;35m',
bcyan = ' \033[1;36m',
bwhite = '\033[1;37m',
lamd = "\033[1;34m"
orange = "\033[1;33m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
yellow = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
banner = f'''
{xduong}██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗      ██████╗ █████╗ ██████╗ ██╗██╗      █████╗  ██████╗
{do2}██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██╔════╝     ██╔════╝██╔══██╗██╔══██╗██║██║     ██╔══██╗██╔════╝
{tim2}█████╔╝ ███████║███████║██╔██╗ ██║██║  ███╗    ██║     ███████║██║  ██║██║██║     ███████║██║     
{yellow2}██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██║   ██║    ██║     ██╔══██║██║  ██║██║██║     ██╔══██║██║     
{luc}██║  ██╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝    ╚██████╗██║  ██║██████╔╝██║███████╗██║  ██║╚██████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝
                                   Bản Quyền By KhangCadilac \t   
                        ╔══════════════════════════════════════════════╗ {xn2}
                        ||➽ Facebook:NguyenHuuKhang.Profile\t      || {trang}        
                        ||➽ Telegram:@nhk1510z\t                      ||     {hong}
                        ||➽ Gmail:huukhangz.info\t              ||        {do2}
                        ╚══════════════════════════════════════════════╝  {yellow}                         

'''


dau="\033[1;31m[\033[1;37m×.×\033[1;31m]\033[1;37m➽"
thanh ="======================================"
thanhxau = white + red +"[" + yellow + "⟨⟩" + red + "] " + white + "➩ "
thanhdep = white + red +"[" + green + "✓" + red + "] " + white + "➽ "
thanhmeo = "\033[1;31m[\033[1;37m=.=\033[1;31m]\033[1;37m=>"
#========= Cấu hình TikTok & Brave =========#
TIKTOK_URL = "https://www.tiktok.com/"
FOLLOWING_URL = "https://www.tiktok.com/following"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_URL = "https://www.tiktok.com/@{user}"






#========= Nhập Cookie =========#
os.system('cls')
print(banner)
def dang_nhap_tiktok():
    """
    Hàm xử lý đăng nhập TikTok bằng cookie.
    Returns:
        list: Danh sách các cookie đã được xử lý
    """
    os.system('cls')
    print(banner)
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
                su_dung_cu = input(f"{trang}Bạn muốn sử dụng cookie cũ không (Y/N) ").strip().upper()
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
  # Xóa lỗi khỏi màn hình
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

            return {
                'success': True,
                'username': username,
                'nickname': nickname,
                'follower_count': followers_count.group(1) if followers_count else 'N/A',
                'following_count': following_count.group(1) if following_count else 'N/A'
            }
        return {'success': False, 'message': 'Cookie không hợp lệ hoặc đã hết hạn'}



def countdown_timer(seconds, message):
    for i in range(seconds, 0, -1):
        print(f"\r{message} {i} giây...", end='', flush=True)
        time.sleep(1)
    print('\r' + ' ' * 80, end='\r')

def unfollowtheo_danhsach(driver, usernames):
    delay_min = int(input('Nhập Delay Min: '))
    delay_max = int(input('Nhập Delay Max: '))
    jobs_to_rest = int(input('Sau bao nhiêu nhiệm vụ thì kích hoạt chống block: '))
    rest_time = int(input(f'Sau {jobs_to_rest} nhiệm vụ thì nghỉ ngơi bao nhiêu giây: '))

    count_success = 0
    failed_accounts = []
    account_thaydoiusername = []

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    failed_file = f"failed_unfollow_{timestamp}.txt"

    task_count = 0

    for user in usernames:
        user_url = f"https://www.tiktok.com/@{user}"
        print(f"{trang}✨ Đang xử lý: {user_url}\033[0m")

        try:
            driver.get(user_url)
            time.sleep(2)

            error_messages = [
                "//p[contains(text(), \"Couldn't find this account\")]",
                "//p[contains(text(), 'Không tìm thấy tài khoản này')]",
                "//div[contains(text(), \"Couldn't find this account\")]"]

            account_not_found = False
            for xpath in error_messages:
                try:
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    if element.is_displayed():
                        print(f"\033[31m⚠️ {user} không tồn tại hoặc đã đổi username, bỏ qua...\033[0m")
                        account_thaydoiusername.append(user)
                        account_not_found = True
                        break
                except TimeoutException:
                    continue

            if account_not_found:
                continue

            FOLLOW_BUTTON = '[data-e2e="follow-button"]:not([aria-label*="Following"])'
            FOLLOWING_BUTTON = '[data-e2e="follow-button"][aria-label*="Following"]'

            try:
                follow_button = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, FOLLOW_BUTTON))
                )
                if follow_button.is_displayed():
                    print(f"\033[33m✅ Bạn đã unfollow rồi, bỏ qua !!!\033[0m")
                    continue
            except (NoSuchElementException, TimeoutException):
                pass

            retry = 0
            while retry < 3:
                try:
                    following_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, FOLLOWING_BUTTON))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", following_button)
                    following_button.click()
                    driver.refresh()
                    time.sleep(2)

                    try:
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, FOLLOW_BUTTON))
                        )
                        count_success += 1
                        task_count += 1
                        print(f"{xl}✅ Bạn đã unfollow {user} ({count_success})\033[0m")
                        break
                    except TimeoutException:
                        retry += 1
                        print(f"{yellow}⚠️ Thử lại unfollow {user} lần {retry}\033[0m")

                except Exception as e:
                    print(f"{red}❌ Lỗi khi thử unfollow {user}: {str(e)}\033[0m")
                    break

            if retry == 3:
                print(f"\033[31m❌ Hiện tại không thể unfollow {user} được.\033[0m")
                failed_accounts.append(user)

            if task_count % jobs_to_rest == 0 and task_count != 0:
                countdown_timer(rest_time, f"🔄 Nghỉ ngơi chống block trong")
            else:
                delay = random.randint(delay_min, delay_max)
                countdown_timer(delay, f"⏳ Đang đợi")

        except Exception as e:
            print(f"\033[31m⚠️ Có lỗi xảy ra với {user}: {str(e)}\033[0m")
            continue

    unique_accounts = set(failed_accounts)
    with open(failed_file, 'w', encoding='utf-8') as f:
        for account in unique_accounts:
            f.write(f"Username: {account}\n")

    print(f"{trang}📊 Tổng kết:\033[0m")
    print(f"{trang} Đã lưu danh sách tài khoản unfollow thất bại vào file: {failed_file}")
    print(f"{xl}✅ Số tài khoản đã unfollow thành công: {count_success}\033[0m")
    print(f"{red}❌ Số tài khoản không thể unfollow: {len(failed_accounts)}\033[0m")
    print(f"{yellow}🔄 Số tài khoản có thể đã đổi username: {len(account_thaydoiusername)}\033[0m")


#=======Sau khi đăng nhập thành công========
def menu(webdriver):
    while True:
        print(f"{trang}Bạn muốn sử dụng social nào?:")
        print(f"1. Tiktok{trang}")
        print(f"2. Facebook{trang}")
        print(f"3. Instagram{trang}")
        print(f"4. Thoát{red}")
        print(f"{trang}Nhập lựa chọn của bạn : ", end="", flush=True)
        choice = input()
        if choice == "1": #tiktok
            cookies = dang_nhap_tiktok()
            tiktok = TikTokLogin()
            result = tiktok.login_with_cookie("; ".join(cookies))

            if result['success'] and result['username'] != "N/A":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner)
                print(f"\n{luc}===== Đăng nhập thành công! =====")
                print(f"{trang}Username: {result['username']}")
                print(f"{trang}Link tài khoản: https://www.tiktok.com/@{result['username']}")
                print(f"{trang}Số người theo dõi: {result['follower_count']}")
                print(f"{trang}Số người đang theo dõi: {result['following_count']}")
                print(f"={xl}" * 50)

                #========= Khởi chạy Brave (Debug Mode) =========#
                def chay_brave():
                    subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)

                time.sleep(1)  # Chờ một chút trước khi mở trình duyệt
                chay_brave()
                #========= Cấu hình Selenium =========#
                options = Options()
                options.binary_location = BRAVE_PATH
                options.add_argument("--mute-audio")
                options.add_argument("--disable-sound")
                options.debugger_address = "127.0.0.1:9222"

                driver = webdriver.Chrome(options=options)

                #========= Đăng nhập Cookie vào Brave (Selenium) =========#
                driver.get(TIKTOK_URL)  # Cần mở trang trước khi thêm cookie
                ActionChains(driver).key_down(Keys.CONTROL).send_keys('m').key_up(Keys.CONTROL).perform()
                total_cookies = 0
                for item in cookies:
                    name, value = item.split('=', 1)
                    driver.add_cookie({"name": name, "value": value, "domain": ".tiktok.com"})
                    total_cookies += 1

                driver.refresh()
                time.sleep(0.75)

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner)
                print("[❌] Bạn đã nhập sai cookie! Vui lòng nhập lại.")
                exit()

            while True:
                os.system('cls')
                print(banner)
                print(f"\n{luc}===== Đăng nhập thành công! =====")
                print(f"{trang}Username: {result['username']}")
                print(f"{trang}Link tài khoản: https://www.tiktok.com/@{result['username']}")
                print(f"{trang}Số người theo dõi: {result['follower_count']}")
                print(f"{trang}Số người đang theo dõi: {result['following_count']}")
                print(f"={xl}" * 50)
                print(f"{yellow}Bạn muốn sử dụng tôi làm gì?(TIKTOK)(hoặc nhập 'back' để về menu)")
                print(f"1. Unfollow bằng danh sách{trang}")
                print(f"2. Quay lại{trang}")
                print(f"{trang}Nhập lựa chọn của bạn : ", end="", flush=True)
                tiktok_choice = input()

                if tiktok_choice == "1":
                    usernames = docdanhsach()
                    unfollowtheo_danhsach(driver, usernames)
                    exit()
                elif tiktok_choice == "2":
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")  # Xóa dòng nhập sai
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="") 
                    break
                elif tiktok_choice == 'back':
                    nhap_nhay()
                    print(" " * 50, end="\r")
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")
                    menu(webdriver)
                    break
                else:
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")  # Xóa dòng nhập sai
                    print("\033[F\033[K", end="")
                    print("\033[F\033[K", end="")  # Xóa thông báo lỗi
                    for _ in range(5): print(f"{red}Vui lòng nhập đúng lựa chọn!", end="\r", flush=True); time.sleep(0.2); print(" " * 30, end="\r", flush=True); time.sleep(0.2)
                    continue
        elif choice == "2":
            print("Đây là facebook")
            break
        elif choice =="3":
            print("Đây là instagram")
            break
        elif choice == "4":
            print("Tạm biệt!")
            driver.quit()
            break
        else:
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")  # Xóa dòng nhập sai
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")  # Xóa thông báo lỗi
            for _ in range(5): print(f"{red}Vui lòng nhập đúng lựa chọn!", end="\r", flush=True); time.sleep(0.2); print(" " * 30, end="\r", flush=True); time.sleep(0.2)
            print(" " * 50, end="\r")  # Xóa lỗi khỏi màn hình

def nhap_nhay():
    for _ in range(5):  # Số lần nhấp nháy
        print("Đang quay lại menu chính.....", end="\r")
        time.sleep(0.2)  # Giảm thời gian xuống 0.2 giây
        print(" " * 30, end="\r")
        time.sleep(0.2)
def docdanhsach():
    while True:
        try:
            print(f"{trang}Nhập đường dẫn chứa file danh sách following (hoặc nhập 'back' để về menu):")
            duongdanfile = input(f"{trang}Nhập: ").strip()

            if duongdanfile.lower() == 'back':
                nhap_nhay()  
                print(" " * 50, end="\r")
                print("\033[F\033[K", end="")
                print("\033[F\033[K", end="")
                print("\033[F\033[K", end="")
                print("\033[F\033[K", end="")  
                print("\033[F\033[K", end="")
                print("\033[F\033[K", end="")  
                menu(webdriver)
                break

            usernames = []
            with open(duongdanfile, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.startswith("Username: "):
                        username = line.replace("Username: ", "").strip()
                        if username != "N/A":
                            usernames.append(username)

            if usernames:  # Nếu có username hợp lệ, return danh sách
                print(f"{trang}Số lượng username đọc được: {len(usernames)}")
                return usernames
            else:
                print("File không chứa username hợp lệ. Vui lòng nhập lại.")
        except FileNotFoundError:
            print("\033[F\033[K", end="")  # Xóa dòng nhập sai
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")  # Xóa thông báo lỗi
            print(f"{red}Bạn đã nhập sai đường dẫn,vui lòng nhập lại!!", end="\r", flush=True)  # In lỗi mà không xuống dòng
            time.sleep(2)  # Hiển thị lỗi trong 2 giây
            print(" " * 50, end="\r")
            continue
menu(webdriver)


