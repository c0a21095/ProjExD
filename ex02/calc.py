import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk() #ウィンドウを作成
root.title("電卓") #ウィンドウ名を設定
root.geometry("400x600") #ウィンドウサイズを設定
entry = tk.Entry(root, justify="right", width=10, font=("", 40)) #入力欄を描画
entry.grid(row=0,column=0, columnspan=4)#4グリッドに跨って描画
ope_list = ["+", "-", "*", "/", "."] #演算子のリスト


#ボタンを押されたときに表示するメッセージボックスの関数
def button_click(event):
    btn = event.widget
    txt = btn["text"] #text部分を取得
    check = entry.get() #入力情報を取得
    if txt == "C": #クリアボタンが押されたならば
        entry.delete(0, tk.END) #結果を削除する
    elif txt == "=": #イコールなら
            formula = entry.get() #文字列を取得
            res = eval(formula) #数式なら、計算する
            entry.delete(0, tk.END) #表示内容を削除する
            entry.insert(tk.END, res) #結果を挿入する
    elif txt not in ope_list: #数字ボタンが押されたならば
        entry.insert(tk.END, txt) #押された文字列を挿入する
    else: #それ以外(クリアボタン,数字ボタン以外)の場合
        if len(check) == 0 or check[-1] in ope_list: #演算子が連続するか、先頭に来るなら
            pass #入力を受け付けない
        else: #そうでなければ
            entry.insert(tk.END, txt) #押された文字列を挿入する


r, c = 2, 2 #rowとcolumnの初期値を設定
for num in range(9, -1, -1):
    #ボタンを描画する。(ウィンドウインスタンス、ボタンの文字列、フォントタイプ・サイズ、幅、高さ)
    num = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)

    #ボタンとメッセージボックスのイベントを紐づける
    num.bind("<1>", button_click)

    #ボタンを配置する。grid(row=行数、column=列数)、左上が(0,0)で下(右)に行くにつれて増える
    num.grid(row=r, column=c)
    c -= 1
    if c%3 == 2: #左端に来たら
        r += 1 #1行下に
        if r == 5:
            c = 0 #0の時だけ真ん中にする
        else:
            c = 2 #それ以外は右端に戻す

#四則演算,クリアボタンを実装
operators = [
    ["C", "1", "0"], #クリアボタンの文字,row,column
    ["/", "1", "3"], #割り算ボタンの文字,row,column
    ["*", "2", "3"], #掛け算ボタンの文字,row,column
    ["-", "3", "3"], #引き算ボタンの文字,row,column
    ["+", "4", "3"], #足し算ボタンの文字,row,column
    ["=", "5", "3"], #イコールボタンの文字,row,column
    [".", "5", "2"], #小数点の文字,row,column
    ["00", "5", "1"]] #00ボタンの文字,row,column

for i in range(len(operators)): #リストの要素ぶん回す
    buttun = tk.Button(root, text=f"{operators[i][0]}", font=("", 30), width=4, height=2)
    buttun.bind("<1>", button_click)
    buttun.grid(row=int(operators[i][1]), column=int(operators[i][2])) #ボタンを描画,配置

root.mainloop() #ウィンドウを表示