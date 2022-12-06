import tkinter as tk
import tkinter.messagebox as tkm


def main():
    root = tk.Tk() #ウィンドウを作成
    root.title("迷えるこうかとん") #ウィンドウ名を設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black") #キャンバスを描画
    canvas.pack() #キャンバスをpackする
    cx, cy = 300, 400 #こうかとんのx座標,y座標
    kokaton = tk.PhotoImage(file="fig/8.png") #こうかとんの画像ファイルを指定
    key = "" #変数keyを空文字""で初期化
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton") #キャンバス上にこうかとんを配置
    root.mainloop() #ウィンドウを表示


#コマンドラインから実行されたら
if __name__ == "__main__":
    main() #main関数を呼び出し