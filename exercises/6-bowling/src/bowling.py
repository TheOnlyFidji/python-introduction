class strike():
    def __init__(self, id):
        self.id = id

    def calc(self, scores):
        score = scores[self.id+1]+scores[self.id+2]
        return score

class spare():
    def __init__(self, id):
        self.id = id

    def calc(self, scores):
        score = scores[self.id+1]
        return score

class regular():
    def __init__(self, id):
        self.id = id

    def calc(self, scores):
        return 0

def bowling_score(frames: str):
    rounds = []
    scores = []
    reg = False

    chars = list(frames)
    for char in chars:
        match char:
            case "X":
                rounds.append(strike(len(scores)))
                scores.append(10)
            case "/":
                rounds.append(spare(len(scores)))
                scores.append(10 - (scores[len(scores) - 1]))
                reg = False
            case " ":
                reg = False
            case _:
                if not reg:
                    reg = True
                    if char == "-":
                        scores.append(0)
                    else:
                        scores.append(int(char))
                else:
                    reg = False
                    rounds.append(regular(len(scores) - 1))
                    if char == "-": scores.append(0)
                    else: scores.append(int(char))

    count = 0
    total = 0
    for round in rounds:
            if count < 9: total += round.calc(scores)
            count += 1

    total += sum(scores)
    return total
