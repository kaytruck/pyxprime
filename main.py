import pyxel
import common


class Main:
    def __init__(self) -> None:
        self.question: int = 2 * 3 * 5 * 7
        self.answer: str = "2*3*5*7"

        self.num_x_offsets = {
            "0": common.NUM_X_0,
            "1": common.NUM_X_1,
            "2": common.NUM_X_2,
            "3": common.NUM_X_3,
            "4": common.NUM_X_4,
            "5": common.NUM_X_5,
            "6": common.NUM_X_6,
            "7": common.NUM_X_7,
            "8": common.NUM_X_8,
            "9": common.NUM_X_9,
            "*": common.OPE_X_MUL,
        }

        pyxel.init(common.WINDOW_WIDTH, common.WINDOW_HEIGHT, caption="PyxPrime")
        pyxel.load("assets/pyxprime.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btn(pyxel.KEY_SPACE):
            self.answer = ""

    def draw(self) -> None:
        pyxel.cls(3)
        # 問題領域
        self.draw_num_area(str(self.question), 8, 8, 112, 32, 11, 7)
        # 回答領域
        self.draw_num_area(self.answer, 8, 48, 112, 32, 6, 7)
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
        pyxel.text(14, 121, "[SPC]", 0)
        pyxel.rect(48, 112, 32, 16, 15)
        pyxel.text(52, 114, "BckSpc", 0)
        pyxel.text(56, 121, "[BS]", 0)
        pyxel.rect(88, 112, 32, 16, 15)
        pyxel.text(95, 114, "ENTER", 0)
        pyxel.text(95, 121, "[ENT]", 0)

    def draw_num_area(self, s: str, x, y, w, h, area_col, ch_bg_col) -> None:
        pyxel.rect(x, y, w, h, area_col)
        draw_len: int = len(s) * 16
        str_x: int = common.WINDOW_WIDTH // 2 - draw_len // 2
        for i, v in enumerate(s):
            num_x = self.num_x_offsets[v]
            num_y = common.NUM_Y
            if v == "*":
                num_y = common.OPE_Y

            if num_x != -1:
                pyxel.blt(str_x + (i * 16), (y + 8), 0, num_x, num_y, 16, 16, ch_bg_col)


Main()
