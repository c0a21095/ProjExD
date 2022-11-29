import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk() #ウィンドウを作成
root.title("tk") #ウィンドウ名を設定
root.geometry("300x500") #ウィンドウサイズを設定

entry = tk.Entry(root, justify="right", width=10, font=("", 40)) #入力欄を描画
entry.grid(row=0,column=0, columnspan=3)#3グリッドに跨って描画


#ボタンを押されたときに表示するメッセージボックスの関数
def button_click(event):
    btn = event.widget
    txt = btn["text"] #text部分を取得
    if num == "=": #イコールなら
        pass
    else: #イコール以外のボタンなら
        #tkm.showinfo(txt, f"{txt}のボタンがクリックされました")
        entry.insert(tk.END, txt)



r, c = 1, 0
for num in range(9, -1, -1):
    #ボタンを描画する。(ウィンドウインスタンス、ボタンの文字列、フォントタイプ・サイズ、幅、高さ)
    num = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)

    #ボタンとメッセージボックスのイベントを紐づける
    num.bind("<1>", button_click)

    #ボタンを配置する。grid(row=行数、column=列数)、左上が(0,0)で下(右)に行くにつれて増える
    num.grid(row=r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["+", "="] #+と=のリストを作成
for ope in operators: #リストの要素ぶん回す
    buttun = tk.Button(root, text=f"{ope}", font=("", 30), width=4, height=2)
    buttun.bind("<1>", button_click)
    buttun.grid(row=r, column=c) #ボタンを描画,配置
    c += 1
    if c%3 == 0:
        r += 1
        c = 0


root.mainloop() #ウィンドウを表示