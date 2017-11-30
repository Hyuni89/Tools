import sys

def show(l):
    for element in l:
        for sub in element:
            print(sub, end="\t")
        print()

def tran(l, t):
    flag = True
    if t == "stick":
        flag = False
    
    ret = []
    for element in l:
        if flag is True and element[5] != "수동":
            ret.append(element)
        if flag is False and element[5] == "수동":
            ret.append(element)
    
    return ret

def num(l, w, t, n):
    index = -1
    if w == 0:  # mile
        index = 3
    elif w == 1: # year
        index = 2
    elif w == 2: # price
        index = 4

    ret = []
    for element in l:
        number = -1
        if w == 0 or w == 2:
            number = int("".join(filter(str.isdigit, element[index])))
        else:
            if "." in element[index]:
                number = int(element[index].split(".")[0])
            else:
                number = int(element[index])
            
        if t == 0 and number >= n: # >
            ret.append(element)
        if t == 1 and number <= n: # <
            ret.append(element)
    
    return ret


reg = []
with open("log") as f:
    for line in f.readlines():
        reg.append(line.strip().split("|"))

if len(sys.argv) > 1:
    for arg in sys.argv:
        if "--" in arg:
            command = str()
            element = str()
            if "=" in arg:
                command, element = arg.split("=")
            command = command[2:]
            
            if command == "tran":
                reg = tran(reg, element)
            elif command == "mile":
                reg = num(reg, 0, 0 if element[0] == ">" else 1, int(element[1:]))
            elif command == "year":
                reg = num(reg, 1, 0 if element[0] == ">" else 1, int(element[1:]))
            elif command == "price":
                reg = num(reg, 2, 0 if element[0] == ">" else 1, int(element[1:]))
            elif command == "all":
                break
    
    show(reg)
else:
    print("Usage: filter.py <args> ...")
    print("%-30s" % "\t--all", end="")
    print("%-50s" % "show all")
    print("%-30s" % "\t--tran=(stick | auto)", end="")
    print("%-50s" % "choose transmission")
    print("%-30s" % "\t--mile=(>|<)[num]", end="")
    print("%-50s" % "set limit mile")
    print("%-30s" % "\t--year=(>|<)[num]", end="")
    print("%-50s" % "set limit year")
    print("%-30s" % "\t--price=(>|<)[num]", end="")
    print("%-50s" % "set limit price")