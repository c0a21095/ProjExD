import pygame as pg
import sys
#必要なモジュールをインポート


#ゲームの処理を書く
def main():
    clock = pg.time.Clock() #時間計測用のオブジェクト

    #初期配置
    pg.display.set_caption("逃げろ！こうかとん") #ウィンドウ名
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウサイズ
    pg_bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像を指定
    pg_bg_rct = pg_bg_sfc.get_rect() #rectを取り出す

    tori_sfc = pg.image.load("fig/6.png") #surfaceオブジェクトとして画像を読み込む
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0) #画像の大きさを変える。画像surface,回転角,大きさの比率
    tori_rct = tori_sfc.get_rect() #rectを取り出す
    tori_rct.center = 900, 400 #400,300の位置に配置する
    scrn_sfc.blit(tori_sfc, tori_rct) #scrn_sfcにtori_sfcを貼り付ける。tori_rctに従って

    #Trueになるまで繰り返す
    while True:
        scrn_sfc.blit(pg_bg_sfc, pg_bg_rct) #rectに従い背景を設定
        for event in pg.event.get():
            #×ボタンが押されたら
            if event.type == pg.QUIT:
                return #main関数からreturnする
        pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない
        clock.tick(1000) #1秒あたり1000フレームの時を刻む(whileに制限をかける)


if __name__ == "__main__":
    pg.init() #pygameモジュールを初期化(毎回やる)
    main() #main関数を呼び出し
    pg.quit() #pygameモジュールを終了する(毎回やる)
    sys.exit() #必須ではないが、念のため終了させる。