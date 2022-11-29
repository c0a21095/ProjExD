import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk() #ウィンドウを作成
root.title("tk") #ウィンドウ名を設定
root.geometry("300x500") #ウィンドウサイズを設定


#ボタンを押されたときに表示するメッセージボックスの関数
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンがクリックされました")


r, c = 0, 0
for num in range(9, -1, -1):
    #ボタンを描画する。(ウィンドウインスタンス、ボタンの文字列、フォントタイプ・サイズ、幅、高さ)
    num = tk.Button(root, text=str(num), font=("", 30), width=4, height=2)

    #ボタンとメッセージボックスのイベントを紐づける
    num.bind("<1>", button_click)

    #ボタンを配置する。grid(row=行数、column=列数)、左上が(0,0)で下(右)に行くにつれて増える
    c += 1
    num.grid(row=r, column=c)
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop() #ウィンドウを表示