with open("day5/input.txt",'r') as f:
    tab = []
    dp = []
    for line in f:
        line = line.strip().split()
        if line == []:
            tab.append(dp)
            dp = []
            continue
        dp.append(line)
    tab.append(dp)
    seed = list(map(int, tab[0][0][1:]))
    cond = [ [0 for i in range(1,10)] for i in range(len(seed))]
    for cont in range(len(tab)):
        for nb in tab[cont][1:]:
            nb = list(map(int, nb))
            for s in range(len(seed)):
                #print(nb[0] + nb[2])
                if nb[1] <= seed[s] <= nb[1] + nb[2] and cond[s][cont] == 0:
                    cond[s][cont] = 1
                    seed[s] += nb[0] - nb[1]
    print(min(seed))
    #print(tab)
