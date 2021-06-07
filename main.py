import pyxel
import random
import common
from status import Status


class Main:
    def __init__(self) -> None:
        self.question: int = 0
        self.answer_str: str = ""
        self.answer_list = []
        self.timer: int = 0
        self.score: int = 0
        self.status = Status.TITLE
        self.msgcolor: int = 8
        self.fail_cnt: int = 0
        self.renew_cnt: int = 0
        self.question_area_col = 11
        self.answer_area_col = 6

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

        pyxel.init(
            common.WINDOW_WIDTH,
            common.WINDOW_HEIGHT,
            caption="PyxPrime",
            fps=common.FPS,
        )
        pyxel.load("assets/pyxprime.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.msgcolor = 10 if pyxel.frame_count % 20 == 1 else 8
        if self.status == Status.TITLE:
            self.update_title()
        elif self.status == Status.GAMING:
            self.update_gaming()
        elif self.status == Status.TIMEUP:
            self.update_timeup()

    def update_title(self):
        """update(タイトル画面)"""
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.status = Status.GAMING
            self.timer = 0
            self.question: int = self.create_question()

    def update_gaming(self):
        """update(ゲーム中)"""
        # タイマー更新
        if pyxel.frame_count % common.FPS == 1:
            self.timer += 1
        if self.timer >= common.TIMELIMIT:
            self.status = Status.TIMEUP
            return
        if pyxel.btn(pyxel.KEY_SPACE):
            # スペースキーで回答を全消去
            self.answer_list = []
        if len(self.answer_list) < 4:
            # 数字キー入力
            if pyxel.btnp(pyxel.KEY_2):
                self.answer_list.append(2)
            if pyxel.btnp(pyxel.KEY_3):
                self.answer_list.append(3)
            if pyxel.btnp(pyxel.KEY_5):
                self.answer_list.append(5)
            if pyxel.btnp(pyxel.KEY_7):
                self.answer_list.append(7)
        if len(self.answer_list) > 0:
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                # BSキーで直前に入力した数字を消去
                self.answer_list = self.answer_list[0:-1]
            if pyxel.btnp(pyxel.KEY_ENTER):
                # 割り算の実行
                if self.calc():
                    self.score += 1
                    # 次の問題の生成
                    self.question = self.create_question()
                self.answer_list = []

        self.update_answer_str()

        # 問題領域の背景色を設定
        if self.renew_cnt > 0:
            # 問題更新時の色
            self.renew_cnt -= 1
            self.question_area_col = common.QUESTION_AREA_BLINK_COL
        else:
            self.question_area_col = common.QUESTION_AREA_COL

        # 回答領域の背景色を設定
        if self.fail_cnt > 0:
            # 誤答時の色
            self.fail_cnt -= 1
            self.answer_area_col = common.ANSWER_AREA_BLINK_COL
        else:
            self.answer_area_col = common.ANSWER_AREA_COL

    def update_timeup(self):
        self.update_title()

    def calc(self):
        """計算実行

        問題の数値を回答の数値で割る。

        Returns:
            True:計算結果が1になった, False:それ以外
        """
        answer: int = 1
        for a in self.answer_list:
            answer *= a
        if self.question % answer == 0:
            self.question //= answer
        else:
            # 誤答
            self.fail_cnt = common.BLINK_CNT_LIMIT
        return True if self.question == 1 else False

    def create_question(self):
        """問題生成

        Returns:
            問題数値
        """
        self.renew_cnt = common.BLINK_CNT_LIMIT
        question: int = 1
        for _ in range(random.randint(1, 4)):
            question *= random.choice([2, 3, 5, 7])
        return question

    def update_answer_str(self):
        """回答文字列生成

        回答が入力された配列から、回答文字列を生成する。
        """
        self.answer_str = ""
        for a in self.answer_list:
            self.answer_str += str(a)
            self.answer_str += "*"
        if len(self.answer_str) > 1 and self.answer_str[-1] == "*":
            self.answer_str = self.answer_str[0:-1]

    def draw(self) -> None:
        """画面描画"""
        pyxel.cls(3)
        # タイマー
        pyxel.text(8, 8, "TIME: " + str(self.timer), 0)
        # スコア
        pyxel.text(50, 8, "SCORE: " + str(self.score), 0)
        # 問題領域
        self.draw_num_area(
            str(self.question),
            8,
            common.QUESTION_AREA_Y,
            112,
            32,
            self.question_area_col,
            7,
        )
        # 回答領域
        self.draw_num_area(
            self.answer_str, 8, common.ANSWER_AREA_Y, 112, 32, self.answer_area_col, 7
        )
        # 数字入力ボタン
        pyxel.rect(8, common.NUMKEY_AREA_Y, 16, 16, 14)
        pyxel.blt(8, common.NUMKEY_AREA_Y, 0, common.NUM_X_2, common.NUM_Y, 16, 16, 7)
        pyxel.rect(40, common.NUMKEY_AREA_Y, 16, 16, 14)
        pyxel.blt(40, common.NUMKEY_AREA_Y, 0, common.NUM_X_3, common.NUM_Y, 16, 16, 7)
        pyxel.rect(72, common.NUMKEY_AREA_Y, 16, 16, 14)
        pyxel.blt(72, common.NUMKEY_AREA_Y, 0, common.NUM_X_5, common.NUM_Y, 16, 16, 7)
        pyxel.rect(104, common.NUMKEY_AREA_Y, 16, 16, 14)
        pyxel.blt(104, common.NUMKEY_AREA_Y, 0, common.NUM_X_7, common.NUM_Y, 16, 16, 7)
        # 操作入力ボタン
        pyxel.rect(8, common.BTN_AREA_Y, 32, 16, 15)
        pyxel.text(14, common.BTN_NAME_Y, "CLEAR", 0)
        pyxel.text(14, common.BTN_KEY_Y, "[SPC]", 0)
        pyxel.rect(48, common.BTN_AREA_Y, 32, 16, 15)
        pyxel.text(52, common.BTN_NAME_Y, "BckSpc", 0)
        pyxel.text(56, common.BTN_KEY_Y, "[BS]", 0)
        pyxel.rect(88, common.BTN_AREA_Y, 32, 16, 15)
        pyxel.text(95, common.BTN_NAME_Y, "ENTER", 0)
        pyxel.text(95, common.BTN_KEY_Y, "[ENT]", 0)

        if self.status == Status.TITLE:
            # タイトル画面の表示
            pyxel.text(20, 70, "Press [Space] To Start.", self.msgcolor)
        elif self.status == Status.TIMEUP:
            # クリア画面の表示
            pyxel.text(50, 60, "TIME UP!!", self.msgcolor)
            pyxel.text(16, 70, "Press [Space] To Restart.", self.msgcolor)

    def draw_num_area(self, s: str, x, y, w, h, area_col, ch_bg_col) -> None:
        """問題および回答領域描画

        問題領域、または回答領域の数式を描画する。

        Args:
            s: 出力する文字列
            x:
            y:
            w:
            h:
            area_col: 表示領域の背景色
            ch_bg_col: イメージバンクの文字の背景色(透過色)
        """
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
