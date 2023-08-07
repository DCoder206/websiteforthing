def check(l):
    if sorted(l[0:2]) == sorted(l[2:4]):
        return 1
    elif sorted(l[0:2]) == sorted(l[4:6]):
        return 2
    else:
        return 0

l = None
while l != "exit":
    l = input("-> ")
    if l == "exit":
        break
    print(check(eval(l)))
