import string # Used to import character list


file = open("input.txt", "r")

# ! Initial Test
# line = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
# c1 = line[:int(len(line)/2)]
# c2 = line[int(len(line)/2):]
# print(c1)
# print(c2)

priority = 0
alphabet = string.ascii_letters

for line in file:
    c1 = line[:int(len(line)/2)]
    c2 = line[int(len(line)/2):]

    duplicate = None
    for item in c1:
        if item in c2:
            duplicate = item
            break

    priority += alphabet.index(duplicate) + 1

print(priority)
