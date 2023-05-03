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


if __name__ == '__main__':
    label1, label2, label3, label4, label5, label6 = map(int, input().split())
    dice = Dice(label1, label2, label3, label4, label5, label6)
    dirs = input()
    for direction in dirs:
        dice.roll(direction)
    print(dice.label1)
