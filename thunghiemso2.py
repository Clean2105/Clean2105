# Tử nghiệm số 2 là BeautifulSoup4 lần 2
# https://vjol.info.vn/index/en/

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://vjol.info.vn"

FALLBACK_HTML = """
<h3>Tạp chí Khoa học và Công nghệ Đại học Đà Nẵng</h3>
<p><strong>Tạp chí của Đại học Đà Nẵng</strong> <a href="https://vjol.info.vn">View Journal</a></p>
<h3>Tạp chí Khoa học Trường Đại học Tân Tạo</h3>
<p><strong>Tạp chí của Trường Đại học Tân Tạo</strong> <a href="https://vjol.info.vn">View Journal</a></p>
<h3>Tạp chí Kinh tế và Phát triển</h3>
<p><strong>Tạp chí của Đại học Kinh tế Quốc dân</strong> <a href="https://vjol.info.vn">View Journal</a></p>
"""

class VJOL:
    IGNORED = {"developed by", "language", "aims and scope", "journal subjects"}

    def __init__(self, base_url=BASE_URL, max_urls=1000):
        self.base_url = base_url
        self.max_urls = max_urls

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        rows = []

        for h3 in soup.find_all("h3"):
            name = h3.get_text(strip=True)
            if not name or name.lower() in self.IGNORED:
                continue

            sibling = h3.find_next_sibling()
            desc, link = "", ""
            if sibling:
                strong = sibling.find(["strong", "b"])
                desc = (strong or sibling).get_text(strip=True)
                a_tag = sibling.find("a", href=True)
                if a_tag:
                    link = urljoin(self.base_url, a_tag["href"])

            rows.append({"Tên Tạp Chí": name, "Cơ Quan Chủ Quản": desc, "Liên Kết": link})

        return rows

    def save_excel(self, rows, path="danh_sach_tap_chi_vjol.xlsx"):
        if not rows:
            print("[!] Không có dữ liệu để lưu.")
            return
        pd.DataFrame(rows).to_excel(path, index=False)
        print(f"[+] Đã lưu {len(rows)} dòng vào {path}")

    def __call__(self, html):
        rows = self.parse(html)
        self.save_excel(rows)
        urls = [r["Liên Kết"] for r in rows if r["Liên Kết"]]
        return urls[: self.max_urls]

def fetch(url, timeout=10):
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        return resp.text
    except requests.RequestException as e:
        print(f"[!] Lỗi mạng: {e}")
        return None

if __name__ == "__main__":
    print("[-] Đang kết nối tới VJOL...")
    html = fetch(BASE_URL)
    if not html:
        print("[!] Chuyển sang HTML dự phòng.")
        html = FALLBACK_HTML

    urls = VJOL(max_urls=100)(html)
    print(urls)