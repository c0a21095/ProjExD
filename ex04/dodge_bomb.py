import pygame as pg
import sys
import random
#必要なモジュールをインポート


#ゲームの処理を書く
def main():
    clock = pg.time.Clock() #時間計測用のオブジェクト

    #初期配置
    pg.display.set_caption("逃げろ！こうかとん") #ウィンドウ名
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウサイズ
    scrn_rct = scrn_sfc.get_rect() #rectを取り出す
    pg_bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像を指定
    pg_bg_rct = pg_bg_sfc.get_rect() #rectを取り出す
    scrn_sfc.blit(pg_bg_sfc, pg_bg_rct) #rectに従い背景を設定

    tori_up = pg.image.load("fig/6.png") #上向きのこうかとん
    tori_down = pg.image.load("fig/8.png") #下向きのこうかとん
    tori_reft = pg.image.load("fig/5.png") #左向きのこうかとん
    tori_right = pg.image.load("fig/2.png") #右向きのこうかとん
    tori_sfc = pg.image.load("fig/0.png") #surfaceオブジェクトとして画像を読み込む,初期状態
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率
    tori_rct = tori_sfc.get_rect() #rectを取り出す
    tori_rct.center = 900, 400 #900,400の位置に配置する
    scrn_sfc.blit(tori_sfc, tori_rct) #scrn_sfcにtori_sfcを貼り付ける。tori_rctに従って

    #1つ目の爆弾
    bomb1_sfc = pg.Surface((20, 20)) #空のsurfaceオブジェクトを作成
    bomb1_sfc.set_colorkey((0, 0, 0)) #背景の黒色を消す
    bombx, bomby = 10, 10 #爆弾の大きさを指定
    pg.draw.circle(bomb1_sfc, (255, 0 ,0), (10, 10), 10) #円を作成。surface,色,中心,半径
    bomb1_rct = bomb1_sfc.get_rect() #rectを取り出す
    bomb1_rct.centerx = random.randint(bombx, scrn_rct.width-bombx) #x座標をランダムに
    bomb1_rct.centery = random.randint(bomby, scrn_rct.height-bomby) #y座標をランダムに
    scrn_sfc.blit(bomb1_sfc, bomb1_rct) #爆弾を貼り付け
    vx1, vy1 = 1, 1 #移動速度を設定

    #2つめの爆弾
    bomb2_sfc = pg.Surface((20, 20)) #空のsurfaceオブジェクトを作成
    bomb2_sfc.set_colorkey((0, 0, 0)) #背景の黒色を消す
    pg.draw.circle(bomb2_sfc, (255, 0 ,0), (10, 10), 10) #円を作成。surface,色,中心,半径
    bomb2_rct = bomb2_sfc.get_rect() #rectを取り出す
    bomb2_rct.centerx = random.randint(bombx, scrn_rct.width-bombx) #x座標をランダムに
    bomb2_rct.centery = random.randint(bomby, scrn_rct.height-bomby) #y座標をランダムに
    scrn_sfc.blit(bomb2_sfc, bomb2_rct) #爆弾を貼り付け
    vx2, vy2 = 1, 1 #移動速度を設定

    count_fonto = pg.font.Font(None, 75) #時間の文字の大きさを設定

    while True:
        scrn_sfc.blit(pg_bg_sfc, pg_bg_rct) #rectに従い背景を設定
        #すべてのイベントを取得
        for event in pg.event.get():
            #×ボタンが押されたら
            if event.type == pg.QUIT:
                return #main関数からreturnする
        key_dict = pg.key.get_pressed() #すべてのキーの入力状態に関する辞書を返す
        if key_dict[pg.K_UP]    and tori_rct.top-1    > scrn_rct.top: #上キーが押され、移動先が壁でなければ
            tori_rct.centery -= 1 #上方向に移動
            tori_sfc = tori_up #上向きのこうかとんに設定
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率
        if key_dict[pg.K_DOWN]  and tori_rct.bottom+1 < scrn_rct.bottom: #下キーが押され、移動先が壁でなければ
            tori_rct.centery += 1 #下方向に移動
            tori_sfc = tori_down #下向きのこうかとんに設定
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率
        if key_dict[pg.K_LEFT]  and tori_rct.left-1   > scrn_rct.left: #左キーが押され、移動先が壁でなければ
            tori_rct.centerx -= 1 #左方向に移動
            tori_sfc = tori_reft #左向きのこうかとんに設定
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率
        if key_dict[pg.K_RIGHT] and tori_rct.right+1  < scrn_rct.right: #右キーが押され、移動先が壁でなければ
            tori_rct.centerx += 1 #右方向に移動
            tori_sfc = tori_right #右向きのこうかとんに設定
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率

        scrn_sfc.blit(tori_sfc, tori_rct) #scrn_sfcにtori_sfcを貼り付ける。tori_rctに従って

        bomb1_rct.move_ip(vx1, vy1) #爆弾をvx,vyぶん移動させる
        scrn_sfc.blit(bomb1_sfc, bomb1_rct) #爆弾を貼り付け
        yoko1, tate1 = check_bound(bomb1_rct, scrn_rct) #反射の関数を呼び出し
        vx1 *= yoko1 #x軸の移動方向を反映
        vy1 *= tate1 #y軸の移動方向を反映
        bomb2_rct.move_ip(vx2, vy2) #爆弾をvx,vyぶん移動させる
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) #爆弾を貼り付け
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct) #反射の関数を呼び出し
        vx2 *= yoko2 #x軸の移動方向を反映
        vy2 *= tate2 #y軸の移動方向を反映

        time_txt = "survival time:" + str(pg.time.get_ticks()//1000) + "sec" #時間として表示する文字列を設定
        count_txt = count_fonto.render(time_txt, True, (0, 0, 0)) #文字をrenderする
        scrn_sfc.blit(count_txt, (0, 0)) #文字を表示

        if tori_rct.colliderect(bomb1_rct) or tori_rct.colliderect(bomb2_rct): #もし爆弾とこうかとんがぶつかったら
            gameover(clock, scrn_sfc, scrn_rct, count_fonto) #gameover関数を呼び出す
            return #main関数を終える
        
        pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない
        clock.tick(1000) #1秒あたり1000フレームの時を刻む(whileに制限をかける)


#反射するか否かを決める関数
def check_bound(obj_rct, scr_rct):
    #範囲内なら+1,範囲外なら-1
    yoko, tate = 1, 1 #タテとヨコを初期化
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: #左右が範囲外になったら
        yoko = -1 #逆方向に
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: #上下が範囲外になったら
        tate = -1 #逆方向に
    return yoko, tate #タテとヨコを返す


#ゲームオーバー時に呼び出される関数
def gameover(clock, scrn_sfc, scrn_rct, count_fonto):
    gmor_fonto = pg.font.Font(None, 300) #ゲームオーバーの文字の大きさを設定
    gmor_txt = gmor_fonto.render("GAME OVER", True, (0, 0, 255)) #文字をrenderする
    gmor_txt_rct = gmor_txt.get_rect(center=(scrn_rct.right//2, scrn_rct.bottom//2)) #真ん中に文字を配置
    scrn_sfc.blit(gmor_txt, gmor_txt_rct) #文字を貼り付け
    pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない
    clock.tick(0.33) #3秒間表示


if __name__ == "__main__":
    pg.init() #pygameモジュールを初期化(毎回やる)
    main() #main関数を呼び出し
    pg.quit() #pygameモジュールを終了する(毎回やる)
    sys.exit() #必須ではないが、念のため終了させる。