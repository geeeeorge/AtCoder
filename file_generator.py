from pathlib import Path


class FileGenerator:
    """
    〜操作方法〜
    ① インスタンス作成
    ② 作成するファイルのメソッドを呼ぶ
    ③ メソッドがなければ，自分で追加する
    """

    def __init__(self, contest_name, contest_number):
        # コンテスト名
        self.contest_name = contest_name
        # 何回目のコンテストか
        self.contest_number = contest_number

    def generate_file(self, contest_folder_path, number_length):
        """ファイルを作成．直接は叩かない

        Args:
            contest_folder_path (Path): 親のパス
            number_length (int): 問題数
        """
        for i in range(number_length):
            # Pathの設定
            make_py_file = Path(F'/Users/george/Documents/AtCoder/{self.contest_name.upper()}/{contest_folder_path}/{chr(65 + i)}.py')

            # Pythonのファイルを生成
            make_py_file.parent.parent.mkdir(exist_ok=True)
            make_py_file.parent.mkdir(exist_ok=True)
            make_py_file.touch()

    def abc(self):
        self.generate_file(
            contest_folder_path=Path(F'{self.contest_name.upper()}{self.contest_number}'),
            number_length=6,
            )

    def arc(self):
        self.generate_file(
            contest_folder_path=Path(F'{self.contest_name.upper()}{self.contest_number}'),
            number_length=6,
            )

    def agc(self):
        self.generate_file(
            contest_folder_path=Path(F'{self.contest_name.upper()}{self.contest_number}'),
            number_length=6,
            )

    def past(self):
        self.generate_file(
            contest_folder_path=Path(F'第{self.contest_number}回アルゴリズム実技検定'),
            number_length=15,
            )

    def typical90(self):
        for i in range(1, self.contest_number+1):
            # Pathの設定
            if i < 10:
                make_py_file = Path(F'/Users/george/Documents/AtCoder/{self.contest_name.upper()}/0{i}.py')
            else:
                make_py_file = Path(F'/Users/george/Documents/AtCoder/{self.contest_name.upper()}/{i}.py')

            # Pythonのファイルを生成
            make_py_file.parent.parent.mkdir(exist_ok=True)
            make_py_file.parent.mkdir(exist_ok=True)
            make_py_file.touch()


if __name__ == '__main__':
    # file_generator = FileGenerator('abc', 232)
    # file_generator.abc()
    file_generator = FileGenerator('typical90', 90)
    file_generator.typical90()
