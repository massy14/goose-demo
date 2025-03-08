# Flappy Bird Game

Pythonとpygameを使用した簡単なFlappy Birdクローンゲームです。

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

## 今後の実装予定

- [ ] 障害物（パイプ）の追加
- [ ] 衝突判定の実装
- [ ] スコア表示の追加