import pygame as pg
import random
import sys
# 必要なモジュールをインポート

#色のデータ
color_data = {
    "red" :  (255,   0,   0),
    "blue":  (  0,   0, 255),
    "black": (  0,   0,   0),
    "green": (  0, 255,   0)
}

BOMB = 5 #爆弾の数


#画面描画のクラス
class Screen():
    # 初期メソッド (タイトル、幅・高さタプル、背景画像ファイル名)
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) #ウィンドウ名
        self.sfc = pg.display.set_mode(wh) #ウィンドウサイズ
        self.rct = self.sfc.get_rect() #rectを取り出す
        self.bgi_sfc = pg.image.load(img_path) #背景画像
        self.bgi_rct = self.bgi_sfc.get_rect() #rectを取り出す
    
    # 背景設定のメソッド
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) #背景を設定


# こうかとんのクラス
class Bird():
    #キーが押されたときに動く方向をまとめた辞書 key_delta
    key_delta = {
        pg.K_UP:    [0, -2, "fig/6.png"],
        pg.K_DOWN:  [0, +2, "fig/8.png"],
        pg.K_LEFT:  [-2, 0, "fig/5.png"],
        pg.K_RIGHT: [+2, 0, "fig/2.png"],
    }

    #初期メソッド (画像ファイル名、拡大率、初期座標タプル)
    def __init__(self, img_path, ratio, xy):
        self.ratio = ratio
        self.sfc = pg.image.load(img_path) #画像を読み込む
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio) #画像の大きさを変更
        self.rct = self.sfc.get_rect() #rectを取り出す
        self.rct.center = xy #初期座標に配置

    # こうかとん描画のメソッド(背景に描画するため、Screenをもってくる)
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) #こうかとんを描画

    # こうかとんの位置を更新するメソッド
    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed() #すべてのキーの入力状態の辞書をもらう
        # 4方向に対して入力状態を判定
        for key, delta in Bird.key_delta.items():
            if key_dct[key]: #もし該当キーが押されていたら
                self.rct.centerx += delta[0] #x方向に移動
                self.rct.centery += delta[1] #y方向に移動
                self.sfc = pg.image.load(delta[2]) #画像を読み込む
                self.sfc = pg.transform.rotozoom(self.sfc, 0, self.ratio) #画像の大きさを変更
            if check_bound(self.rct, scr.rct) != (+1, +1): #行き先が壁であれば
                self.rct.centerx -= delta[0] #x方向の移動を相殺
                self.rct.centery -= delta[1] #y方向の移動を相殺
        self.blit(scr) #こうかとんを描画(上記のblitメソッド呼び出し)


# 爆弾のクラス
class Bomb():
    #初期メソッド (色タプル、半径、速度タプル、Screenオブジェクト)
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空の画面を描画
        self.sfc.set_colorkey(color_data["black"]) #背景色(黒)
        pg.draw.circle(self.sfc, color_data[color], (rad, rad), rad) #爆弾を描く
        self.rct = self.sfc.get_rect() #rectを取り出す
        self.rct.centerx = random.randint(0, scr.rct.width) #ランダムなx座標に配置
        self.rct.centery = random.randint(0, scr.rct.height) #ランダムなy座標に配置
        self.vx, self.vy = vxy #速度タプルから速度を設定

    # 爆弾描画のメソッド(背景に描画するため、Screenをもってくる)  
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) #爆弾を描画

    # 爆弾の位置を更新するメソッド
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate = check_bound(self.rct, scr.rct) #壁かどうかチェック
        self.vx *= yoko
        self.vy *= tate #移動方向を反映
        self.blit(scr) #こうかとんを描画(上記のblitメソッド呼び出し)


#時間計測のクラス
class Time():
    def update(self, scr:Screen):
        self.fonto = pg.font.Font(None, 75) #時間の文字の大きさを設定
        self.txt = "survival time:" + str(pg.time.get_ticks()//1000) + "sec" #時間として表示する文字列を設定
        self.rct = self.fonto.render(self.txt, True, color_data["black"]) #文字をrenderする
        scr.sfc.blit(self.rct, (0, 0)) #文字を表示


#壁判定の関数
def check_bound(obj_rct, scr_rct):
    """
    第1引数:こうかとんrectまたは爆弾rect
    第2引数:スクリーンrect
    範囲内：+1/範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


#ゲームオーバー時に呼び出される関数
def gameover(clock, scr:Screen):
    gmor_fonto = pg.font.Font(None, 300) #ゲームオーバーの文字の大きさを設定
    txt = "GAME OVER"
    gmor_txt = gmor_fonto.render(txt, True, color_data["blue"]) #文字をrenderする
    gmor_txt_rct = gmor_txt.get_rect(center=(scr.rct.right//2, scr.rct.bottom//2)) #真ん中に文字を配置
    scr.sfc.blit(gmor_txt, gmor_txt_rct) #文字を貼り付け
    pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない
    clock.tick(0.33) #3秒間表示


#ゲームクリア時に呼び出される関数(未実装)
def gameclear(clock, scr:Screen):
    gmor_fonto = pg.font.Font(None, 300) #ゲームオーバーの文字の大きさを設定
    txt = "GAME CLEAR"
    gmor_txt = gmor_fonto.render(txt, True, color_data["green"]) #文字をrenderする
    gmor_txt_rct = gmor_txt.get_rect(center=(scr.rct.right//2, scr.rct.bottom//2)) #真ん中に文字を配置
    scr.sfc.blit(gmor_txt, gmor_txt_rct) #文字を貼り付け
    pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない
    clock.tick(0.33) #3秒間表示


#main関数
def main():
    clock =pg.time.Clock()
    atk_tim = 0
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")
    bombs = []
    for i in range(BOMB):
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        bomb = Bomb("red", 15, (vx, vy), scr)
        bomb.update(scr)
        bombs.append(bomb)
    bird = Bird("fig/0.png", 2.0, (900,400))
    bird.update(scr)
    time = Time()
    if pg.mixer:
        music = "ex05\data\house_lo.wav" #bgmのファイル名
        pg.mixer.music.load(music) #bgmを流す準備
        pg.mixer.music.play(-1) #bgmを流す。-1で無限ループ

    while True:
        scr.blit()
        key_dct = pg.key.get_pressed() #すべてのキーの入力状態の辞書をもらう
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        bird.update(scr)
        time.update(scr)
        for bomb in bombs:
            bomb.update(scr)
            if bird.rct.colliderect(bomb.rct) and pg.time.get_ticks()//1000 > 1:
                gameover(clock, scr)
                return
            if len(bombs)==0:  
                gameclear(clock, scr)
        #以下、爆弾を削除する機能(未実装)
        if pg.time.get_ticks()%1000==0:
            atk_tim += 1
        if atk_tim >= 3 and key_dct[pg.K_SPACE]:
            del bombs[-1]
            atk_tim = 0
            for bomb in bombs:
                bomb.update(scr)
        #以上、爆弾を削除する機能
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()