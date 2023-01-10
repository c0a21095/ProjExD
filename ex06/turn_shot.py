import pygame as pg
import sys
#必要なモジュールをインポート

#色のデータ
color_data = {
    "red" :  (255,   0,   0),
    "blue":  (  0,   0, 255),
    "black": (  0,   0,   0),
    "green": (  0, 255,   0),
    "white": (255, 255, 255),
}

#画面描画用のクラス
class Screen():
    #初期化関数(タイトル名、縦横幅、画像パス)
    def __init__(self, title, wh):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
    
    #画像の描画関数
    def blit(self):
        #背景を黒色に塗りつぶす
        self.sfc.fill(color_data["black"])
        #背景の中央に白線を描く
        pg.draw.line(self.sfc, color_data["white"],
         (self.rct.centerx, 0),
         (self.rct.centerx, 900), 10)

#プレイヤー1用のクラス
class Player():
    #キーと方向の対応付け辞書
    key_delta = [{
        pg.K_w:     [0, -1],
        pg.K_s:     [0, +1],
        pg.K_a:     [-1, 0],
        pg.K_d:     [+1, 0],
    } , {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],        
    }]

    #初期化関数(画像のパス、拡大率、x座標、y座標)
    def __init__(self, color, rad, xy, no):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey(color_data["black"])
        pg.draw.circle(self.sfc, color_data[color], (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.pre_key = [1, 0] #以前の方向を記憶する変数
        self.number = no #どちらのプレイヤーか判定
        if self.number:
            self.bullet_direction = [-1, 0] #左方向に弾が移動するように
        else:
            self.bullet_direction = [+1, 0] #右方向に弾が移動するように
        self.bullets = [] #弾のリスト

    #プレイヤーの描画関数(画面オブジェクト)
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    #プレイヤーの情報更新関数(画面オブジェクト)
    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        #プレイヤーの移動
        for key, delta in Player.key_delta[self.number].items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            #壁なら行かせないようにする
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)

    #弾を設置する処理を行う関数
    def set_bullet(self, scr:Screen):
        if len(self.bullets) < 10: #設置上限を10に
            self.bullets.append(Projectile("blue", 20, self.bullet_direction, self)) #弾を追加


#弾用のクラス
class Projectile:
    #初期化関数(色、半径、移動方向、Playerのオブジェクト)
    def __init__(self, color, rad, vxy, player):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey(color_data["black"])
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = player.rct.centerx
        self.rct.centery = player.rct.centery
        self.vx, self.vy = vxy
    
    #弾の描画関数(画像のオブジェクト)
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    #弾の情報更新関数(画像のオブジェクト)
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        scr.sfc.blit(self.sfc, self.rct)
        width, height = check_bound(self.rct, scr.rct)
        return width == -1 or height == -1


#オブジェクトの境界判定
def check_bound(obj_rct, scr_rct):
    width, height = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        width = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        height = -1
    return width, height


#ゲームオーバー時に呼び出される関数(中村実装)
def gameover(clock, player, scr:Screen):
    font = pg.font.Font(None, 300) #ゲームオーバーの文字の大きさを設定
    txt = f"{player} WIN!" #表示する文字列
    txt_rend = font.render(txt, True, (128,   0, 128)) #文字を紫色でrenderする。
    txt_rect = txt_rend.get_rect(center=(scr.rct.right//2, scr.rct.bottom//2)) #真ん中に文字を配置する
    scr.sfc.blit(txt_rend, txt_rect) #文字を貼り付け
    pg.display.update() #ディスプレイ全体を更新。これをしないと文字が表示されない。
    clock.tick(0.33) #3秒間表示する

#メイン関数
def main():
    clock = pg.time.Clock()
    scr = Screen("turn_shot", (1500,900))
    p1 = Player("red", 30, (375, 450), 0)
    p2 = Player("green", 30, (1125, 450), 1)
    counter = 8000

    #メインループ
    while True:
        scr.blit()
        key_dct = pg.key.get_pressed()
        for event in pg.event.get():
            #終了判定
            if event.type == pg.QUIT:
                return
            #eを押したとき
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q and counter >= 4000:
                    p1.set_bullet(scr)
                if event.key == pg.K_m and counter >= 4000:
                    p2.set_bullet(scr)
        
        if counter < 0:
            counter += 8000
        elif counter < 4000:
            #プレイヤー1の衝突判定
            for bullet in p1.bullets:
                if bullet.update(scr):
                    p1.bullets.pop(p1.bullets.index(bullet))
                if bullet.rct.colliderect(p2.rct):
                    gameover(clock, "Player1", scr)
                    return
            #プレイヤー2の衝突判定
            for bullet in p2.bullets:
                if bullet.update(scr):
                    p2.bullets.pop(p2.bullets.index(bullet))
                if bullet.rct.colliderect(p1.rct):
                    gameover(clock, "Player2", scr)
                    return
        else:
            for bullet in p1.bullets:
                bullet.blit(scr)
            for bullet in p2.bullets:
                bullet.blit(scr)

        p1.update(scr)
        p2.update(scr)


        pg.display.update()
        eta = clock.tick(1000)
        counter -= eta


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()