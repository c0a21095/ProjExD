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
    global cx, cy, mx, my, count, kokaton #こうかとんの座標,マス番号をグローバル宣言
    if key == "Up"    and maze_lst[mx][my-1] != 1: #上キーが押され、移動先が壁でなければ
            my -= 1 #上方向へ移動する
            count += 1 #手数をカウント
            kokaton = tk.PhotoImage(file="fig/6.png") #上向きのこうかとんに設定
    if key == "Down"  and maze_lst[mx][my+1] != 1: #下キーが押され、移動先が壁でなければ
            my += 1 #下方向へ移動する
            count += 1 #手数をカウント
            kokaton = tk.PhotoImage(file="fig/8.png") #下向きのこうかとんに設定
    if key == "Left"  and maze_lst[mx-1][my] != 1: #左キーが押され、移動先が壁でなければ
            mx -= 1 #左方向へ移動する
            count += 1 #手数をカウント
            kokaton = tk.PhotoImage(file="fig/5.png") #左向きのこうかとんに設定
    if key == "Right" and maze_lst[mx+1][my] != 1: #右キーが押され、移動先が壁でなければ
            mx += 1 #右方向へ移動する
            count += 1 #手数をカウント
            kokaton = tk.PhotoImage(file="fig/2.png") #右向きのこうかとんに設定
    cx, cy = mx*100+50, my*100+50 #マス単位で移動するように値を代入
    canvas.delete("kokaton") #前に描いたこうかとんを削除
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton") #キャンバス上にこうかとんを配置
    #canvas.coords("kokaton", cx, cy) #tag"kokaton"を動かす
    if cx == 1350 and cy == 750: #ゴールにたどり着いたら
        tkm.showinfo("ゲームクリア",f"ゴールにたどり着きました！あなたは{count}手でゴールしました") #メッセージボックスを表示
    else: #ゴールにたどり着かなかったら
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
    kokaton = tk.PhotoImage(file="fig/0.png") #こうかとんの画像ファイルを指定
    key = "" #変数keyを空文字""で初期化
    count = 0 #手数をカウント,初期値0
    start = canvas.create_rectangle(100,100,200,200,fill="green", tags="goal") #緑色のスタートを表示
    goal  = canvas.create_rectangle(1300,700,1400,800,fill="red", tags="goal") #赤色のゴールを表示
    #canvas.create_image(cx, cy, image=kokaton, tag="kokaton") #キャンバス上にこうかとんを配置
    root.bind("<KeyPress>", key_down) #keyが押されたらkey_down関数を呼び出す
    root.bind("<KeyRelease>", key_up) #keyが離されたらkey_up関数を呼び出す
    main_proc() #main_proc関数を呼び出す
    root.mainloop() #ウィンドウを表示