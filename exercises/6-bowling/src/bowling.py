def converter(char: str) -> int:
    match char:
        case "-": return 0
        case "X": return 10
        case _: return int(char)

class Strike:
    def __init__(self, throw1 : str, throw2 : str):
        self.throw1 = converter(throw1)

        if throw2 == "/": self.throw2 = 10 - self.throw1
        else: self.throw2 = converter(throw2)

    def calc(self):
        return 10 + self.throw1 + self.throw2

class Spare:
    def __init__(self, throw1 : str):
       self.throw1 = converter(throw1)

    def calc(self):
        return 10 + self.throw1

class Regular:
    def __init__(self, throw1, throw2):
        self.throw1 = converter(throw1)
        self.throw2 = converter(throw2)

    def calc(self):
        return self.throw1 + self.throw2

def bowling_score(frames: str):
    score = 0
    frames = frames.split()
    i = 0
    for frame in frames[0:10]:
        if frame == "X":
            if frames[i+1] == "X": score += Strike(10, frames[i+2][:1]).calc()
            else: score += Strike(frames[i+1][:1], frames[i+1][1:]).calc()
        elif frame.endswith("/"):
            score += Spare(frames[i+1][:1]).calc()
        else:
            score += Regular(frame[:1], frame[1:]).calc()
        i += 1

    return score