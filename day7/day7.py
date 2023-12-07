def part1():
    with open('day7/input.txt', 'r') as f:
        hands = []
        order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2' : 2}
        for line in f:
            line = line.split()
            m = 0
            for i in range(len(line[0])):
                #print(line[0], line[0].count(line[0][i])*1000 + order[line[0][i]]*(i+1)*100)
                m += line[0].count(line[0][i])*10000000000000000000 + order[line[0][i]]*(100**(len(line[0])-i-1))
            line.append(m)
            hands.append(line)
        hands.sort(key=lambda x: x[2])
        s = 0
        print(hands)
        for i in range(len(hands)):
            #print(int(hands[i][1]),(i+1))
            s += int(hands[i][1])*(i+1)
        print(s)

def part2():
    with open('day7/input.txt', 'r') as f:
        hands = []
        order = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2' : 2}
        for line in f:
            line = line.split()
            m = 0
            joker = line[0].count('J')
            ma = 0
            for i in line[0]:
                if i != 'J':
                    if ma < max(ma, line[0].count(i)):
                        ma = max(ma, line[0].count(i))
                        l = i
            print(ma, line[0])
            for i in range(len(line[0])):
                #print(line[0], line[0].count(line[0][i])*1000 + order[line[0][i]]*(i+1)*100)
                if line[0][i] == 'J':
                    m += (ma+joker)*10000000000000000000 + order[line[0][i]]*(100**(len(line[0])-i-1))
                elif line[0][i] == l:
                    m += (line[0].count(line[0][i])+joker)*10000000000000000000 + order[line[0][i]]*(100**(len(line[0])-i-1))
                else:
                    m += (line[0].count(line[0][i]))*10000000000000000000 + order[line[0][i]]*(100**(len(line[0])-i-1))
            line.append(m)
            hands.append(line)
        hands.sort(key=lambda x: x[2])
        s = 0
        print(hands)
        for i in range(len(hands)):
            #print(int(hands[i][1]),(i+1))
            s += int(hands[i][1])*(i+1)
        print(s)

part2()