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

    def right(self, top: int, front: int):
        if top == label1:
            if front == label2:
                return label3
            elif front == label3:
                return label5
            elif front == label5:
                return label4
            elif front == label4:
                return label2
        elif top == label2:
            if front == label1:
                return label4
            elif front == label4:
                return label6
            elif front == label6:
                return label3
            elif front == label3:
                return label1
        elif top == label3:
            if front == label1:
                return label2
            elif front == label2:
                return label6
            elif front == label6:
                return label5
            elif front == label5:
                return label1
        elif top == label4:
            if front == label1:
                return label5
            elif front == label5:
                return label6
            elif front == label6:
                return label2
            elif front == label2:
                return label1
        elif top == label5:
            if front == label1:
                return label3
            elif front == label3:
                return label6
            elif front == label6:
                return label4
            elif front == label4:
                return label1
        elif top == label6:
            if front == label2:
                return label4
            elif front == label4:
                return label5
            elif front == label5:
                return label3
            elif front == label3:
                return label2
        raise ValueError("Invalid top or front")


if __name__ == '__main__':
    label1, label2, label3, label4, label5, label6 = map(int, input().split())
    dice = Dice(label1, label2, label3, label4, label5, label6)
    Q = int(input())
    for _ in range(Q):
        top, front = map(int, input().split())
        print(dice.right(top, front))
