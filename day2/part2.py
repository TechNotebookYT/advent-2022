file = open("input.txt", "r")
your_score = 0
opp_score = 0

opp_plays = ["A", "B", "C"]
your_plays = ["X", "Y", "Z"]

for line in file:
    opp, you = line.split(" ")
    you = you[0]

    your_increase = your_plays.index(you)*3

    if you == "X":
        if opp == "A":
            your_increase += 3
        elif opp == "B":
            your_increase += 1
        elif opp == "C":
            your_increase += 2
    elif you == "Y":
        your_increase += opp_plays.index(opp)+1
    elif you == "Z":
        if opp == "A":
            your_increase += 2
        elif opp == "B":
            your_increase += 3
        elif opp == "C":
            your_increase += 1
    
    your_score += your_increase

print(your_score)
