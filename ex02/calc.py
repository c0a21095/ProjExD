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


#ボタンのリスト
buttuns = [
    ["0", "5", "0"], #0ボタンの文字,row,column
    ["1", "4", "0"], #1ボタンの文字,row,column
    ["2", "4", "1"], #2ボタンの文字,row,column
    ["3", "4", "2"], #3ボタンの文字,row,column
    ["4", "3", "0"], #4ボタンの文字,row,column
    ["5", "3", "1"], #5ボタンの文字,row,column
    ["6", "3", "2"], #6ボタンの文字,row,column
    ["7", "2", "0"], #7ボタンの文字,row,column
    ["8", "2", "1"], #8ボタンの文字,row,column
    ["9", "2", "2"], #9ボタンの文字,row,column
    ["C", "1", "0"], #クリアボタンの文字,row,column
    ["/", "1", "3"], #割り算ボタンの文字,row,column
    ["*", "2", "3"], #掛け算ボタンの文字,row,column
    ["-", "3", "3"], #引き算ボタンの文字,row,column
    ["+", "4", "3"], #足し算ボタンの文字,row,column
    ["=", "5", "3"], #イコールボタンの文字,row,column
    [".", "5", "2"], #小数点の文字,row,column
    ["00", "5", "1"]] #00ボタンの文字,row,column

for i in range(len(buttuns)): #リストの要素ぶん回す
    buttun = tk.Button(root, text=f"{buttuns[i][0]}", font=("", 30), width=4, height=2)
    buttun.bind("<1>", button_click)
    buttun.grid(row=int(buttuns[i][1]), column=int(buttuns[i][2])) #ボタンを描画,配置

root.mainloop() #ウィンドウを表示