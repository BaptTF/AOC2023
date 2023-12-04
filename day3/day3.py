def detectnumber(line):
    tab = []
    nb = ""
    index = []
    for i in range(len(line)):
        if line[i].isdigit():
            nb += line[i]
            index.append(i)
        elif nb != "":
            nb = int(nb)
            tab.append((nb,index))
            index = []
            nb = ""
        if i == len(line)-1 and nb != "":
            nb = int(nb)
            tab.append((nb,index))
            index = []
            nb = ""
    return tab

def detectsymbol(line):
    tab = []
    for i in range(len(line)):
        if not line[i].isdigit() and line[i] != ".":
            tab.append((line[i],i))
    return tab

def detectsymbol2(line):
    tab = []
    for i in range(len(line)):
        if not line[i].isdigit() and line[i] == "*":
            tab.append((line[i],i))
    return tab

def part1():
    with open("day3/input.txt", 'r') as f:
        tab = []
        number = []
        symbole = []
        sum = 0
        for line in f:
            #print(line.strip())
            tab.append(line.strip())
            number.append(detectnumber(line.strip()))
            symbole.append(detectsymbol(line.strip()))
        for line in range(len(number)):
            #print(line)
            for n in number[line]:
                print(n)
                for i in range(line-1, line+2):
                    if i < len(symbole) and i >= 0:
                        if symbole[i] != []:
                            for j in symbole[i]:
                                if j[1]+1 in n[1] or j[1]-1 in n[1] or j[1] in n[1]:
                                    sum += n[0]
        print(sum)

def part2():
    with open("day3/input.txt", 'r') as f:
        tab = []
        number = []
        symbole = []
        sum = 0
        for line in f:
            #print(line.strip())
            tab.append(line.strip())
            number.append(detectnumber(line.strip()))
            symbole.append(detectsymbol2(line.strip()))
        for line in range(len(number)):
            #print(number[line])
            for s in range(len(symbole[line])):
                exact = 0
                nbtab = []
                for nb in number[line]: 
                    if symbole[line][s][1]+1 in nb[1] or symbole[line][s][1]-1 in nb[1] or symbole[line][s][1] in nb[1]:
                        exact += 1
                        nbtab.append(nb[0])
                for nb in number[line-1]:
                    if symbole[line][s][1]+1 in nb[1] or symbole[line][s][1]-1 in nb[1] or symbole[line][s][1] in nb[1]:
                        exact += 1
                        nbtab.append(nb[0])
                for nb in number[line+1]:
                    if symbole[line][s][1]+1 in nb[1] or symbole[line][s][1]-1 in nb[1] or symbole[line][s][1] in nb[1]:
                        exact += 1
                        nbtab.append(nb[0])
                if exact == 2:
                    sum += nbtab[0] * nbtab[1]
                                # if j[1]+1 in n[1] or j[1]-1 in n[1] or j[1] in n[1]:
                                #     sum += n[0]
        print(sum)

part2()