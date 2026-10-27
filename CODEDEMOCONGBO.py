# KẾT QUẢ CÔNG BỐ DEMO CUỐI CÙNG!
import re, sqlite3, threading, urllib.request
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin
URL, BASE_URL = "https://vjol.info.vn/index/en/", "https://vjol.info.vn"
XLSX, DB = Path("Danh Sách VJOL.xlsx"), Path("VJOL.db")
IGNORED = {"developed by", "language", "aims and scope", "journal subjects"}
FALLBACK_HTML = """<h3>Tạp chí Khoa học và Công nghệ Đại học Đà Nẵng</h3>
<p><strong>Tạp chí của Đại học Đà Nẵng</strong> <a href="/index/en">View</a></p>"""
STOP = {"of", "and", "the", "for", "in", "on", "journal", "science", "tạp", "chí", "của", "và", "khoa", "học"}

def fetch(url, timeout=10):  
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")
    except Exception as e: print(f"[!] Lỗi mạng: {e}")

def parse(html, base=BASE_URL):
    from bs4 import BeautifulSoup  
    rows = []
    for h3 in BeautifulSoup(html, "html.parser").find_all("h3"):
        name, sib = h3.get_text(strip=True), h3.find_next_sibling()
        if not name or name.lower() in IGNORED: continue
        a = h3.find("a", href=True) or (sib.find("a", href=True) if sib else None)
        strong = sib.find(["strong", "b"]) if sib else None
        desc = (strong or sib).get_text(" ", strip=True)[:150] if sib else ""
        rows.append({"Tên Tạp Chí": name, "Cơ Quan Chủ Quản": desc, "Liên Kết": urljoin(base, a["href"]) if a else ""})
    return rows

def scrape():
    import pandas as pd
    print("[-] Đang kết nối tới VJOL..."); html = fetch(URL)
    if not html: print("[!] Chuyển sang HTML dự phòng."); html = FALLBACK_HTML
    rows = parse(html)
    for i, r in enumerate(rows, 1): print(f"{i}. {r['Tên Tạp Chí']}\n   └── {r['Cơ Quan Chủ Quản']}\n")
    if rows: pd.DataFrame(rows).to_excel(XLSX, index=False); print(f"[+] Đã lưu {len(rows)} dòng vào {XLSX}")

def gui():  
    import tkinter as tk; from tkinter import ttk, messagebox, filedialog  
    root = tk.Tk(); root.title("VJOL Scraper"); root.geometry("1000x420")
    var, data, cols = tk.StringVar(value=URL), [], ("Tên", "Mô tả", "Liên kết")
    top = ttk.Frame(root); top.pack(fill="x", padx=8, pady=8)
    tree = ttk.Treeview(root, columns=cols, show="headings")
    def show(rows):
        data[:] = [list(r.values()) for r in rows]; tree.delete(*tree.get_children())
        for r in data: tree.insert("", "end", values=r)
    def load(url):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            root.after(0, show, parse(urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore"), url))
        except Exception as e: root.after(0, messagebox.showerror, "Lỗi mạng", f"{e}\n\nLưu trang bằng Ctrl+S rồi bấm 'Mở file HTML'.")
    def open_html():
        if p := filedialog.askopenfilename(filetypes=[("HTML", "*.html *.htm")]):
            show(parse(open(p, encoding="utf-8", errors="ignore").read(), var.get()))
    def save():
        import pandas as pd
        if data and (p := filedialog.asksaveasfilename(defaultextension=".xlsx")): pd.DataFrame(data, columns=cols).to_excel(p, index=False)
    ttk.Entry(top, textvariable=var).pack(side="left", fill="x", expand=True)
    for t, c in (("Lấy dữ liệu", lambda: threading.Thread(target=load, args=(var.get(),), daemon=True).start()),
                 ("Mở file HTML", open_html), ("Lưu Excel", save)): ttk.Button(top, text=t, command=c).pack(side="left", padx=2)
    for c in cols: tree.heading(c, text=c); tree.column(c, width=320)
    tree.pack(fill="both", expand=True, padx=8, pady=(0, 8)); root.mainloop()

def thong_ke_1(): 
    import matplotlib.pyplot as plt, numpy as np, seaborn as sns
    np.random.seed(1); normal = np.random.normal(0.0, 1.0, 1000)
    mean, median = normal.mean(), np.median(normal)
    print(f"Mean = {mean:.3f} | Median = {median:.3f} | Variance = {normal.var(ddof=1):.3f}")
    plt.figure(figsize=(8, 5)); sns.histplot(normal, kde=True)
    plt.axvline(mean, color="r", label=f"Mean = {mean:.3f}"); plt.axvline(median, color="g", linestyle="--", label=f"Median = {median:.3f}")
    plt.title("VJOL"); plt.legend(); plt.savefig("histogram.png", dpi=120); plt.show()

def thong_ke_2():  
    import matplotlib.pyplot as plt, pandas as pd, seaborn as sns
    if not XLSX.exists(): return print(f"Không tìm thấy {XLSX.resolve()} (hãy chạy mục 1 trước)")
    sns.set_theme(style="whitegrid"); df = pd.read_excel(XLSX, engine="openpyxl"); df.columns = ["ten", "mo_ta", "lien_ket"]
    df.insert(0, "VJOL_ID", range(1, len(df) + 1))
    with sqlite3.connect(DB) as con:
        df.to_sql("VJOL", con, if_exists="replace", index=False); print(f"Đã tạo {DB.resolve()} với {len(df)} dòng")
        print(con.execute("SELECT * FROM VJOL WHERE VJOL_ID = ?", (1,)).fetchone()); d = pd.read_sql_query("SELECT * FROM VJOL", con)
    d["do_dai_ten"], d["do_dai_mo_ta"] = d["ten"].str.len(), d["mo_ta"].fillna("").str.len()
    duoi = d["lien_ket"].fillna("").str.rstrip("/").str.split("/").str[-1]; d["ngon_ngu_lien_ket"] = duoi.where(duoi.isin(["en", "vi"]), "khác")
    tu = Counter(w for t in d["ten"] for w in re.findall(r"\w+", t.lower()) if w not in STOP and len(w) > 2)
    top = pd.DataFrame(tu.most_common(10), columns=["tu", "so_lan"]); fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    sns.histplot(d["do_dai_ten"], kde=True, ax=ax[0, 0]); ax[0, 0].set_title("Độ dài tên tạp chí")
    sns.histplot(d["do_dai_mo_ta"], kde=True, ax=ax[0, 1]); ax[0, 1].set_title("Độ dài mô tả")
    if not top.empty: sns.barplot(data=top, x="so_lan", y="tu", ax=ax[1, 0])
    ax[1, 0].set_title("10 từ xuất hiện nhiều nhất"); sns.countplot(data=d, x="ngon_ngu_lien_ket", ax=ax[1, 1]); ax[1, 1].set_title("Ngôn ngữ liên kết")
    fig.suptitle("VJOL", fontsize=16); fig.tight_layout(); fig.savefig("VJOL_thong_ke.png", dpi=120)
    print(d[["do_dai_ten", "do_dai_mo_ta"]].describe().round(1)); plt.show()

if __name__ == "__main__":
    print("1. Cào dữ liệu VJOL -> Excel\n2. Giao diện Tkinter\n3. Thống kê số 1\n4. Thống kê số 2")
    {"1": scrape, "2": gui, "3": thong_ke_1, "4": thong_ke_2}.get(input("Chọn (1-4): ").strip(), lambda: print("Lựa chọn không hợp lệ"))()