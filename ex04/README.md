# 第4回
## 逃げろこうかとん(ex04/dodge_bomb.py)
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると、1600x900のスクリーンに草原が描かれ、こうかとんを移動させ飛び回る2つの爆弾から逃げるゲーム
- こうかとんがどちらかの爆弾と接触するとゲームオーバーで終了する

### 操作方法
- 矢印キーでこうかとんを上下左右に移動する

### 追加機能
- こうかとんの画像：移動方向によってこうかとんの画像が変化する
- ゲームオーバー時の演出：爆弾とこうかとんが当たったとき、画面にGAME OVERと表示する
- 生存時間表示：生存時間を左上に表示する
- 爆弾の数：爆弾の数を2個に増加(初期から表示)

### ToDo(実装しようと思ったが時間がなかった)
- 爆弾の増加：時間経過によって爆弾を増やす機能
- こうかとんのライフ：1回ではなく、3回触れたらゲームオーバーにするなど、ライフ制度を追加したかった

### メモ
- 特にテキストを実装するとき、pg.display.update()をしてスクリーンを更新しないと一生表示されないので注意！
- 経過時間（クロック数）を取得するとき、pg.time.get_ticks()を用いて取得する