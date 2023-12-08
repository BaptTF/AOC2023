def part1():    
    with open('day8/input.txt') as f:
        d = {}
        directions = f.readline().strip()
        print(directions)
        f.readline()
        for line in f:
            line = line.replace('(','').replace(')','').replace('=','').replace(',', ' ').split()
            d[line[0]] = (line[1],line[2])
        print(d)
        pointer = 'AAA'
        i = 0
        step = 0
        while pointer != 'ZZZ':
            if i >= len(directions):
                i = 0
            letter = directions[i]
            if letter is 'L':
                pointer = d[pointer][0]
            if letter is 'R':
                pointer = d[pointer][1]
            #print(pointer)
            i += 1
            step += 1
        print(step)
    
def part2():
    with open('day8/input.txt') as f:
        d = {}
        directions = f.readline().strip()
        print(directions)
        f.readline()
        for line in f:
            line = line.replace('(','').replace(')','').replace('=','').replace(',', ' ').split()
            d[line[0]] = (line[1],line[2])
        print(d)
        starts = [i for i in d.keys() if i[2] == 'A']
        cycle = []
        for j in starts:
            pointer = j
            i = 0
            step = 0
            while pointer[2] != 'Z':
                if i >= len(directions):
                    i = 0
                letter = directions[i]
                if letter is 'L':
                    pointer = d[pointer][0]
                if letter is 'R':
                    pointer = d[pointer][1]
                #print(pointer)
                i += 1
                step += 1
            cycle.append(step)
        print(cycle)
        from math import gcd
        lcm = 1
        for i in cycle:
            lcm = lcm*i//gcd(lcm, i)
        print(lcm)
part2()