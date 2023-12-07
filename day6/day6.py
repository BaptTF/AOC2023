def part1():
    with open("day6/input.txt", 'r') as f:
        time = list(map(int, f.readline().strip()[9:].split()))
        distance= list(map(int, f.readline().strip()[9:].split()))
        print(time, distance)
        nbRace = len(time)
        win = []
        for nb in range(nbRace):
            ways = 0
            for i in range(time[nb]):
                calcul = (time[nb] - i) * i
                if calcul > distance[nb]:
                    ways += 1
            win.append(ways)
        mul = 1
        for i in win:
            mul *= i
        print(mul)

def part2():
    with open("day6/input.txt", 'r') as f:
        time = f.readline().strip()[9:].split()
        distance = f.readline().strip()[9:].split()
        n = ""
        for t in time:
            n += t
        n = int(n)
        d = ""
        for dist in distance:
            d += dist
        d = int(d)
        print(n, d)
        print(time, distance)
        ways = 0
        for i in range(n):
            calcul = (n - i) * i
            if calcul > d:
                ways += 1
        print(ways)

part2()