import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        # ここでファイルを読み込む処理を実装
        pass

def submit_manual_entry():
    # ここでテキストボックスのデータを取得して処理する
    pass

def enable_submit_button():
    # すべてのテキストボックスが入力された場合に「送信」ボタンをアクティブにする
    pass

# メインウィンドウを作成
root = tk.Tk()
root.title("ユーザー情報管理")

# 上部のボタンの作成
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=0, column=0, columnspan=2, pady=10)

button_file = tk.Button(frame_buttons, text="ユーザー情報変更（申請書読み込み）", command=open_file_dialog)
button_file.pack(side=tk.LEFT)

button_manual = tk.Button(frame_buttons, text="ユーザー情報変更（手動）", command=lambda: frame_manual.grid())
button_manual.pack(side=tk.LEFT)

# 手動入力フレームの作成
frame_manual = tk.Frame(root)

# 各入力フィールドとラベルの作成
labels = ["UserName", "FirstName", "LastName", "E-Mail"]
entries = []
for i, label in enumerate(labels):
    tk.Label(frame_manual, text=label).grid(row=i, column=0, sticky=tk.W, pady=2)
    entry = tk.Entry(frame_manual)
    entry.grid(row=i, column=1, pady=2)
    entries.append(entry)

# 送信ボタン
button_submit = tk.Button(frame_manual, text="送信", state=tk.DISABLED, command=submit_manual_entry)
button_submit.grid(row=len(labels), column=0, columnspan=2, pady=10)

frame_manual.grid(row=1, column=0, columnspan=2)

root.mainloop()
