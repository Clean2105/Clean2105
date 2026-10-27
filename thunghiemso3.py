# Tử nghiệm số 3 là BeautifulSoup4 lần 3
# https://vjol.info.vn/index/en/

import threading, urllib.request, pandas as pd, tkinter as tk
from tkinter import ttk, messagebox, filedialog
from bs4 import BeautifulSoup
from urllib.parse import urljoin
URL = "https://vjol.info.vn/index/en/"
def parse(url, html):
    rows = []
    for a in BeautifulSoup(html, "html.parser").select("h3 a[href]"):
        s = a.find_parent("h3").find_next_sibling()
        rows.append({"Tên": a.get_text(strip=True), "Mô tả": s.get_text(" ", strip=True)[:150] if s else "", "Liên kết": urljoin(url, a["href"])})
    return rows
root = tk.Tk(); root.title("VJOL Scraper"); root.geometry("1000x420")
var, data = tk.StringVar(value=URL), []
top = ttk.Frame(root); top.pack(fill="x", padx=8, pady=8)
tree = ttk.Treeview(root, columns=("Tên", "Mô tả", "Liên kết"), show="headings")
def show(rows):
    data[:] = rows; tree.delete(*tree.get_children())
    for r in rows: tree.insert("", "end", values=list(r.values()))
def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        root.after(0, show, parse(url, urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")))
    except Exception as e:
        root.after(0, messagebox.showerror, "Lỗi mạng", f"{e}\n\nLưu trang bằng Ctrl+S rồi bấm 'Mở file HTML'.")
def open_html():
    if p := filedialog.askopenfilename(filetypes=[("HTML", "*.html *.htm")]):
        show(parse(var.get(), open(p, encoding="utf-8", errors="ignore").read()))
def save():
    if data and (p := filedialog.asksaveasfilename(defaultextension=".xlsx")): pd.DataFrame(data).to_excel(p, index=False)
ttk.Entry(top, textvariable=var).pack(side="left", fill="x", expand=True)
for t, c in (("Lấy dữ liệu", lambda: threading.Thread(target=fetch, args=(var.get(),), daemon=True).start()), ("Mở file HTML", open_html), ("Lưu Excel", save)):
    ttk.Button(top, text=t, command=c).pack(side="left", padx=2)
for c in tree["columns"]: tree.heading(c, text=c); tree.column(c, width=320)
tree.pack(fill="both", expand=True, padx=8, pady=(0, 8))
root.mainloop()