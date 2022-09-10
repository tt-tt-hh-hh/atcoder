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

class NewDice(Dice):
    def __init__(self, sequence):
        super().__init__(sequence)
        self.candidates = []
        for ops in ('', 'N', 'W', 'E', 'S', 'NN'):
            dice = Dice(self.sequence)
            dice.roll(ops)
            for _ in range(4):
                dice.roll('NES')
                self.candidates.append(dice.sequence)

    def __eq__(self, other):
        return min(self.candidates) == min(other.candidates)

prv = []
for _ in range(int(input())):
    tmp = min(NewDice(list(map(int, input().split()))).candidates)
    if tmp in prv:
        print('No')
        exit()
    prv.append(tmp)

print('Yes')