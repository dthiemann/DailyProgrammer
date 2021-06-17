# Daily Programmer
# 5-20-18
# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

def TallyGame(tallyInput):
    players = sorted(list(set(tallyInput.lower())))
    score = {key : 0 for key in players}

    for point in tallyInput:
        if point.isupper():
            score[point.lower()] -= 1
        else:
            score[point.lower()] += 1
    for p in score:
        print(p, score[p])

TallyGame("dbbaCEDbdAacCEAadcB")