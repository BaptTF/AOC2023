def part1():
    file_path = "input.txt"
    with open(file_path, "r") as file:
        c = 0
        for line in file.readlines():
            for i in line:
                if i.isdigit():
                    fdigit = i
                    break
            for i in reversed(line):
                if i.isdigit():
                    ldigit = i
                    break    
            c += int(fdigit+ldigit)
        print(c)

def part2():
    file_path = "input.txt"
    with open(file_path, "r") as file:
        c = 0
        dic = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        for line in file.readlines():
            line = line.strip()
            for i in range(len(line)):
                ffind = False
                if line[i].isdigit():
                    fdigit = line[i]
                    break
                for key in dic.keys():
                    if key in line[:i+1]:
                        fdigit = dic[key]
                        ffind = True
                        break
                if ffind:
                    break
            for i in reversed(range(len(line))):
                lfind = False
                if line[i].isdigit():
                    ldigit = line[i]
                    break
                for key in dic.keys():
                    if key in line[i:]:
                        ldigit = dic[key]
                        lfind = True
                        break
                if lfind:
                    break
            print(fdigit, ldigit)
            c += int(fdigit+ldigit)
        print(c)

if __name__ == "__main__":
    part2()