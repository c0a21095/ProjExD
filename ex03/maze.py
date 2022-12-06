import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
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
    global cx, cy, mx, my #こうかとんの座標,マス番号をグローバル宣言
    if key == "Up"   : my -= 1 #上方向への移動
    if key == "Down" : my += 1 #下方向への移動
    if key == "Left" : mx -= 1 #左方向への移動
    if key == "Right": mx += 1 #右方向への移動
    cx, cy = mx*100+50, my*100+50 #マス単位で移動するように値を代入
    canvas.coords("kokaton", cx, cy) #tag"kokaton"を動かす
    root.after(100, main_proc) #100ミリ秒後にもう一度main_procを動かす


#コマンドラインから実行されたら
if __name__ == "__main__":
    root = tk.Tk() #ウィンドウを作成
    root.title("迷えるこうかとん") #ウィンドウ名を設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black") #キャンバスを描画
    canvas.pack() #キャンバスをpackする

    maze_lst = mm.make_maze(15,9) #15(ヨコ)x9(タテ)の迷路(2次元リスト)を作成,1が壁,0が床
    mm.show_maze(canvas, maze_lst) #作成した迷路を描画する

    mx, my = 1, 1 #マス番号を初期化
    cx, cy = mx*100+50, my*100+50 #こうかとんのx座標,y座標
    kokaton = tk.PhotoImage(file="fig/8.png") #こうかとんの画像ファイルを指定

    key = "" #変数keyを空文字""で初期化
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton") #キャンバス上にこうかとんを配置
    
    root.bind("<KeyPress>", key_down) #keyが押されたらkey_down関数を呼び出す
    root.bind("<KeyRelease>", key_up) #keyが離されたらkey_up関数を呼び出す
    main_proc() #main_proc関数を呼び出す
    root.mainloop() #ウィンドウを表示