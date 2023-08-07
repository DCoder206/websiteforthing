l = eval(input("-> "))
def cchar(c):
    if c == 0:
        return " "
    elif c == 1:
        return "X"
    elif c == 2:
        return "0"
def printer(l):
    print(f"{cchar(l[0])} | {cchar(l[1])} | {cchar(l[2])}")
    print("--+---+--")
    print(f"{cchar(l[3])} | {cchar(l[4])} | {cchar(l[5])}")
    print("--+---+--")
    print(f"{cchar(l[6])} | {cchar(l[7])} | {cchar(l[8])}")

printer(l)
