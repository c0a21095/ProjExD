import tkinter as tk
import tkinter.messagebox as tkm
#必要なモジュールの呼び出し


#key_down関数
def key_down(event):
    global key #keyをグローバル宣言
    key = event.keysym #押されたキーのシンボルをkeyに代入する


#key_up関数
def key_up(event):
    global key #keyをグローバル宣言
    key = "" #keyに空文字を代入,どのキーも押されていないことにする


#リアルタイム処理をするmain_proc関数
def main_proc():
    global cx, cy #こうかとんの座標をグローバル宣言
    if key == "Up"   : cy -= 20 #上方向への移動
    if key == "Down" : cy += 20 #下方向へ移動
    if key == "Left" : cx -= 20 #左方向へ移動
    if key == "Right": cx += 20 #右方向へ移動
    canvas.coords("kokaton", cx, cy) #tag"kokaton"を動かす
    root.after(100, main_proc) #100ミリ秒後にもう一度main_procを動かす


#コマンドラインから実行されたら
if __name__ == "__main__":
    root = tk.Tk() #ウィンドウを作成
    root.title("迷えるこうかとん") #ウィンドウ名を設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black") #キャンバスを描画
    canvas.pack() #キャンバスをpackする
    cx, cy = 300, 400 #こうかとんのx座標,y座標
    kokaton = tk.PhotoImage(file="fig/8.png") #こうかとんの画像ファイルを指定
    key = "" #変数keyを空文字""で初期化
    root.bind("<KeyPress>", key_down) #keyが押されたらkey_down関数を呼び出す
    root.bind("<KeyRelease>", key_up) #keyが離されたらkey_up関数を呼び出す
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton") #キャンバス上にこうかとんを配置
    main_proc() #main_proc関数を呼び出す
    root.mainloop() #ウィンドウを表示