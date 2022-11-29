import tkinter as tk

root = tk.Tk() #ウィンドウを作成
root.title("tk") #ウィンドウ名を設定
root.geometry("300x500") #ウィンドウサイズを設定

#ボタンを描画する。(ウィンドウインスタンス、ボタンの文字列、フォントタイプ・サイズ、幅、高さ)
button_0 = tk.Button(root, text="0", font=("", 30), width=4, height=2)
button_1 = tk.Button(root, text="1", font=("", 30), width=4, height=2)
button_2 = tk.Button(root, text="2", font=("", 30), width=4, height=2)
button_3 = tk.Button(root, text="3", font=("", 30), width=4, height=2)
button_4 = tk.Button(root, text="4", font=("", 30), width=4, height=2)
button_5 = tk.Button(root, text="5", font=("", 30), width=4, height=2)
button_6 = tk.Button(root, text="6", font=("", 30), width=4, height=2)
button_7 = tk.Button(root, text="7", font=("", 30), width=4, height=2)
button_8 = tk.Button(root, text="8", font=("", 30), width=4, height=2)
button_9 = tk.Button(root, text="9", font=("", 30), width=4, height=2)

#ボタンを配置する。grid(row=行数、column=列数)、左上が(0,0)で下(右)に行くにつれて増える
button_0.grid(row=3, column=0)
button_1.grid(row=2, column=2)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=0)
button_4.grid(row=1, column=2)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=0)
button_7.grid(row=0, column=2)
button_8.grid(row=0, column=1)
button_9.grid(row=0, column=0)

root.mainloop() #ウィンドウを表示