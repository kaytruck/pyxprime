import pyxel
import common


class Main:
    def __init__(self) -> None:
        self.question: int = 2 * 3 * 5 * 7
        self.answer: str = "2*3*5*7"

        pyxel.init(common.WINDOW_WIDTH, common.WINDOW_HEIGHT, caption="PyxPrime")
        pyxel.load("assets/pyxprime.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.cls(3)
        # 問題領域
        pyxel.rect(8, 8, 112, 32, 11)
        pyxel.text(10, 16, str(self.question), 0)  # TODO 数値を正しい位置に描画する
        # 回答領域
        self.draw_answer()
        # 数字入力ボタン
        pyxel.rect(8, 88, 16, 16, 14)
        pyxel.blt(8, 88, 0, common.NUM_X_2, common.NUM_Y, 16, 16, 7)
        pyxel.rect(40, 88, 16, 16, 14)
        pyxel.blt(40, 88, 0, common.NUM_X_3, common.NUM_Y, 16, 16, 7)
        pyxel.rect(72, 88, 16, 16, 14)
        pyxel.blt(72, 88, 0, common.NUM_X_5, common.NUM_Y, 16, 16, 7)
        pyxel.rect(104, 88, 16, 16, 14)
        pyxel.blt(104, 88, 0, common.NUM_X_7, common.NUM_Y, 16, 16, 7)
        # 操作入力ボタン
        pyxel.rect(8, 112, 32, 16, 15)
        pyxel.text(14, 114, "CLEAR", 0)
        pyxel.text(14, 121, "[ESC]", 0)
        pyxel.rect(48, 112, 32, 16, 15)
        pyxel.text(52, 114, "BckSpc", 0)
        pyxel.text(56, 121, "[BS]", 0)
        pyxel.rect(88, 112, 32, 16, 15)
        pyxel.text(95, 114, "ENTER", 0)
        pyxel.text(95, 121, "[ENT]", 0)

    def draw_answer(self) -> None:
        pyxel.rect(8, 48, 112, 32, 6)
        answer_len: int = len(self.answer)
        answer_draw_len: int = answer_len * 16
        ans_x: int = common.WINDOW_WIDTH // 2 - answer_draw_len // 2
        for i, s in enumerate(self.answer):
            num_x = -1
            num_y = common.NUM_Y
            if s == "2":
                num_x = common.NUM_X_2
            elif s == "3":
                num_x = common.NUM_X_3
            elif s == "5":
                num_x = common.NUM_X_5
            elif s == "7":
                num_x = common.NUM_X_7
            elif s == "*":
                num_x = 0
                num_y = 32

            if num_x != -1:
                pyxel.blt(ans_x + (i * 16), 56, 0, num_x, num_y, 16, 16, 7)


Main()
