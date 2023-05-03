class Dice:
    label1: int
    label2: int
    label3: int
    label4: int
    label5: int
    label6: int

    def __init__(self, label1: int, label2: int, label3: int, label4: int, label5: int, label6: int):
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.label6 = label6

    def roll(self, direction: str):
        if direction == "N":
            self.label1, self.label2, self.label6, self.label5 = self.label2, self.label6, self.label5, self.label1
        elif direction == "S":
            self.label1, self.label2, self.label6, self.label5 = self.label5, self.label1, self.label2, self.label6
        elif direction == "E":
            self.label1, self.label3, self.label6, self.label4 = self.label4, self.label1, self.label3, self.label6
        elif direction == "W":
            self.label1, self.label3, self.label6, self.label4 = self.label3, self.label6, self.label4, self.label1

    def turn_right(self):
        self.label2, self.label3, self.label5, self.label4 = self.label4, self.label2, self.label3, self.label5

    def __eq__(self, other):
        # dice1とdice2が同一か調べる
        for _ in range(4):
            for _ in range(4):
                if self.label1 == other.label1 and self.label2 == other.label2 and self.label3 == other.label3 and self.label4 == other.label4 and self.label5 == other.label5 and self.label6 == other.label6:
                    return True
                self.roll('E')
            self.roll("N")
        self.turn_right()
        for _ in range(4):
            for _ in range(4):
                if self.label1 == other.label1 and self.label2 == other.label2 and self.label3 == other.label3 and self.label4 == other.label4 and self.label5 == other.label5 and self.label6 == other.label6:
                    return True
                self.roll('E')
            self.roll("N")
        return False

    def print(self):
        print(self.label1, self.label2, self.label3, self.label4, self.label5, self.label6)


if __name__ == '__main__':
    N = int(input())
    dices = []
    for _ in range(N):
        label1, label2, label3, label4, label5, label6 = map(int, input().split())
        dices.append(Dice(label1, label2, label3, label4, label5, label6))

    for i in range(N-1):
        for j in range(i+1, N):
            if dices[i] == dices[j]:
                print("No")
                exit()
    print("Yes")
