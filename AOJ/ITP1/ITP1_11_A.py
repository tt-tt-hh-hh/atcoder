class Dice():
    def __init__(self, sequence):
        self.sequence = sequence

    def move(self, code):
        return [self.sequence[int(idx)] for idx in str(code)]

    def roll(self, root):
        for d in root:
            if d == 'N':
                self.sequence = self.move(152304)
            elif d == 'E':
                self.sequence = self.move(310542)
            elif d == 'S':
                self.sequence = self.move(402351)
            elif d == 'W':
                self.sequence = self.move(215043)

dice = Dice(list(map(int, input().split())))
dice.roll(input())
print(dice.sequence[0])