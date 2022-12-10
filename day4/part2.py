file = open('input.txt', 'r')

full_overlap = 0

for line in file:
    overlap = False
    elf1, elf2 = line.split(",")
    elf1_low, elf1_high = elf1.split("-")
    elf2_low, elf2_high = elf2.split("-")

    # * Set all values to integers
    elf1_low = int(elf1_low)
    elf1_high = int(elf1_high)
    elf2_low = int(elf2_low)
    elf2_high = int(elf2_high)

    # Range Function: range(initial, 1st value you don't want)
    # To make range inclusive of endpts, I added 1
    elf1_nums = [i for i in range(elf1_low, elf1_high+1)]
    elf2_nums = [i for i in range(elf2_low, elf2_high+1)]

    for num in elf1_nums:
        if num in elf2_nums:
            overlap = True
            break
    
    if overlap:
        full_overlap += 1

print(full_overlap)
