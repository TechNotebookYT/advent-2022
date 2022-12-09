file = open("input.txt", "r")
your_score = 0
opp_score = 0

opp_plays = ["A", "B", "C"]
your_plays = ["X", "Y", "Z"]


for line in file:
    m1, m2 = line.split(" ")

    opp_increase = opp_plays.index(m1)+1
    your_increase = your_plays.index(m2[0])+1

    if (opp_increase == your_increase+1) or (opp_increase == 1 and your_increase == 3):
        opp_increase += 6
    elif (your_increase == opp_increase+1) or (your_increase == 1 and opp_increase == 3):
        your_increase += 6
    elif your_increase == opp_increase:
        opp_increase += 3
        your_increase += 3

    opp_score += opp_increase
    your_score += your_increase

print(your_score)
print(opp_score)
