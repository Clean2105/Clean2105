from pathlib import Path
from collections import Counter
import re
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

XLSX = Path("Danh Sách VJOL.xlsx")
DB = Path("VJOL.db")

if not XLSX.exists():
    raise SystemExit(f"Không tìm thấy file: {XLSX.resolve()}")

df = pd.read_excel(XLSX, engine="openpyxl")
df.columns = ["ten", "mo_ta", "lien_ket"]   
df.insert(0, "VJOL_ID", range(1, len(df) + 1))

with sqlite3.connect(DB) as con:
    df.to_sql("VJOL", con, if_exists="replace", index=False)
    print(f"Đã tạo {DB.resolve()} với {len(df)} dòng")

    VJOL_ID = 5 
    row = con.execute(
        "SELECT * FROM VJOL WHERE VJOL_ID = ?", (VJOL_ID,)
    ).fetchone()
    print(row if row else f"Không có bản ghi với VJOL_ID = {VJOL_ID}")

    data = pd.read_sql_query("SELECT * FROM VJOL", con)

data["do_dai_ten"] = data["ten"].str.len()
data["do_dai_mo_ta"] = data["mo_ta"].fillna("").str.len()

duoi = data["lien_ket"].str.rstrip("/").str.split("/").str[-1]
data["ngon_ngu_lien_ket"] = duoi.where(duoi.isin(["en", "vi"]), "khác")

STOP = {"of", "and", "the", "for", "in", "on", "journal", "science",
        "tạp", "chí", "của", "và", "khoa", "học"}
tu = Counter(
    w
    for ten in data["ten"]
    for w in re.findall(r"\w+", ten.lower())
    if w not in STOP and len(w) > 2
)
top_tu = pd.DataFrame(tu.most_common(10), columns=["tu", "so_lan"])

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

sns.histplot(data["do_dai_ten"], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Độ dài tên tạp chí (số ký tự)")

sns.histplot(data["do_dai_mo_ta"], kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Độ dài mô tả (số ký tự)")

sns.barplot(data=top_tu, x="so_lan", y="tu", ax=axes[1, 0])
axes[1, 0].set_title("10 từ xuất hiện nhiều nhất trong tên")

sns.countplot(data=data, x="ngon_ngu_lien_ket", ax=axes[1, 1])
axes[1, 1].set_title("Ngôn ngữ của liên kết")

fig.suptitle("VJOL", fontsize=16)
fig.tight_layout()
fig.savefig("VJOL_thong_ke.png", dpi=120)

print(data[["do_dai_ten", "do_dai_mo_ta"]].describe().round(1))
plt.show()