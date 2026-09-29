import random
def game():
    print("You are playing game...")
    score = random.randint(1,70)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore =int(hiscore)
        else:
            hiscore = 0
    print(f"your score is: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()

