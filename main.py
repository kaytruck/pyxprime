import pyxel
import common


class Main:
    def __init__(self) -> None:
        pyxel.init(common.WINDOW_WIDTH, common.WINDOW_HEIGHT, caption="PyxPrime")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.cls(3)
        # 問題領域
        pyxel.rect(8, 8, 112, 32, 11)
        # 回答領域
        pyxel.rect(8, 48, 112, 32, 6)
        # 数字ボタン
        pyxel.rect(8, 88, 16, 16, 14)
        pyxel.rect(32, 88, 16, 16, 14)
        pyxel.rect(56, 88, 16, 16, 14)
        pyxel.rect(80, 88, 16, 16, 14)
        pyxel.rect(104, 88, 16, 16, 14)
        # 操作ボタン
        pyxel.rect(8, 112, 32, 16, 15)
        pyxel.rect(48, 112, 32, 16, 15)
        pyxel.rect(88, 112, 32, 16, 15)


Main()
