# Tử nghiệm số một là BeautifulSoup4.
# https://vjol.info.vn/index/en/

import requests
from bs4 import BeautifulSoup
url = 'https://vjol.info.vn/index/en/'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    journals = soup.find_all('div', class_='obj_journal_summary')
    
    if not journals:
        journal_titles = soup.find_all('h3')
        print(f"Tìm thấy {len(journal_titles)} tạp chí trên trang:\n")
        
        for index, title in enumerate(journal_titles, 1):
            name = title.get_text(strip=True)
            next_tag = title.find_next_sibling(['p', 'div', 'strong'])
            description = next_tag.get_text(strip=True) if next_tag else "Không có mô tả"
            
            print(f"{index}. {name}")
            print(f"   └── {description}\n")
    else:
        for index, journal in enumerate(journals, 1):
            title_tag = journal.find('h3', class_='title') 
            desc_tag = journal.find('div', class_='description')
            
            name = title_tag.get_text(strip=True) if title_tag else journal.find('h3').get_text(strip=True)
            description = desc_tag.get_text(strip=True) if desc_tag else ""
            
            print(f"{index}. {name}")
            print(f"   └── {description}\n")
else:
    print(f"Không kết nối được.Mã số lỗi: {response.status_code}")