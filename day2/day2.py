nbcube = "12 red cubes, 13 green cubes, and 14 blue cubes"
def part1():
    with open("inputreal.txt", 'r') as f:
        ans = 0
        for line in f:
            lst = line.strip().replace(';',',').replace(":",",").split(",")
            print(lst)
            id = int(lst[0][4:])
            maxg = 0
            maxr = 0
            maxb = 0
            for i in lst[1:]:
                nb = ""
                for j in i[1:]:
                    if j.isdigit():
                        nb += j
                    else:
                        nb = int(nb)
                        break
                if "green" in i:
                    maxg = max(nb, maxg)
                elif "red" in i:
                    maxr = max(nb, maxr)
                elif "blue" in i:
                    maxb = max(nb, maxb)
            if not (maxr > 12 or maxg > 13 or maxb > 14):
                print(f"{id}, red : {maxr}, green : {maxg}, blue : {maxb}")
                ans += id
        print(ans)

def part2():
    with open("inputreal.txt", 'r') as f:
        ans = 0
        for line in f:
            lst = line.strip().replace(';',',').replace(":",",").split(",")
            print(lst)
            id = int(lst[0][4:])
            maxg = 0
            maxr = 0
            maxb = 0
            for i in lst[1:]:
                nb = ""
                for j in i[1:]:
                    if j.isdigit():
                        nb += j
                    else:
                        nb = int(nb)
                        break
                if "green" in i:
                    maxg = max(nb, maxg)
                elif "red" in i:
                    maxr = max(nb, maxr)
                elif "blue" in i:
                    maxb = max(nb, maxb)
            ans += maxr * maxg * maxb
        print(ans)

if __name__ == "__main__":
    part1()
    part2()