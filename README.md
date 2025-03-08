# Flappy Bird Game

Pythonとpygameを使用した簡単なFlappy Birdクローンゲームです。

## 機能

- 青い鳥のキャラクター
- スペースキーによる飛行控除
- 動的な背景（流れる雲）
- 地面との衝突判定
- アニメーションされた背景要素

## 必要条件

- Python 3.x
- pygame

## インストール方法

1. リポジトリをクローン:
```bash
git clone https://github.com/massy14/goose-demo.git
```

2. 仮想環境を作成して有効化:
```bash
python -m venv env
source env/bin/activate  # Linuxの場合
# または
env\Scripts\activate  # Windowsの場合
```

3. 必要なパッケージをインストール:
```bash
pip install pygame
```

## 実行方法

```bash
python flappy_bird.py
```

## 操作方法

- スペースキー: 鳥を上に飛ばす
- ×ボタン: ゲームを終了

## 最新の更新内容

- 空色の背景を追加
- 動く雲のアニメーションを実装
- 緑色の地面と装飾を追加
- 地面との衝突判定を実装

## 今後の実装予定

- [ ] 鳥のグラフィックの改善
- [ ] 背景に山や建物の追加
- [ ] 障害物（パイプ）の追加
- [ ] スコア表示の追加