file = open('input.txt', 'r')

full_contain = 0

for line in file:
    contains = False
    elf1, elf2 = line.split(",")
    elf1_low, elf1_high = elf1.split("-")
    elf2_low, elf2_high = elf2.split("-")

    elf1_low = int(elf1_low)
    elf1_high = int(elf1_high)
    elf2_low = int(elf2_low)
    elf2_high = int(elf2_high)

    if (elf1_low <= elf2_low) and (elf1_high >= elf2_high):
        contains = True
    elif (elf2_low <= elf1_low) and (elf2_high >= elf1_high):
        contains = True

    if contains:
        print(elf1_low, elf1_high, elf2_low, elf2_high, "✔")
    else:
        print(elf1_low, elf1_high, elf2_low, elf2_high, "❌")

    if contains:
        full_contain += 1

print(full_contain)
