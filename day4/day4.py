def part1():
    with open("day4/input.txt", "r") as f:
        sum = 0
        for line in f:
            power = 0
            line = line.strip()
            wnb = line[line.index(":")+1:line.index("|")].split()
            nb = line[line.index("|")+1:len(line)].split()
            for i in nb:
                if i in wnb:
                    power += 1
            if power != 0:
                sum += 2**(power-1)
        print(sum)
    
def part2():
    with open("day4/input.txt", "r") as f:
        tab = []
        for line in f:
            power = 0
            line = line.strip()
            wnb = line[line.index(":")+1:line.index("|")].split()
            nb = line[line.index("|")+1:len(line)].split()
            for i in nb:
                if i in wnb:
                    power += 1
            tab.append(power)
        print(tab)
        scratch = [1 for i in tab]
        print(scratch)
        for i in range(len(tab)):
            for j in range(i+1,i+tab[i]+1):
                if j < len(tab):
                    scratch[j] += scratch[i]
        print(scratch) 
        print(sum(scratch))

part2()