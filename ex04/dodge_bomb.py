import pygame as pg
import sys
#必要なモジュールをインポート


#ゲームの処理を書く
def main():
    clock = pg.time.Clock() #時間計測用オブジェクト

    pg.display.set_caption("逃げろ！こうかとん") #ウィンドウ名
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウサイズ

    pg_bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像を指定

    pg_bg_rct = pg_bg_sfc.get_rect() #rectを取り出す
    scrn_sfc.blit(pg_bg_sfc, pg_bg_rct) #rectに従い背景を設定

    pg.display.update() #ディスプレイ全体を更新。updateしないと表示されない

    clock.tick(1) #1秒あたり1フレームの時を刻む


if __name__ == "__main__":
    pg.init() #pygameモジュールを初期化(毎回やる)
    main() #main関数を呼び出し
    pg.quit() #pygameモジュールを終了する(毎回やる)
    sys.exit() #必須ではないが、念のため終了させる。