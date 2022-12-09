import string  # Used to import character list

file = open("input.txt", "r")
lines = file.readlines()

priority = 0
alphabet = string.ascii_letters

for i in range(100): #100 groups of 3 elves
    elf1 = lines[i*3]
    elf2 = lines[i*3+1]
    elf3 = lines[i*3+2]

    triplicate = None
    for item in elf1:
        if (item in elf2) and (item in elf3):
            triplicate = item
            break
    
    priority += alphabet.index(triplicate) + 1
    
print(priority)
