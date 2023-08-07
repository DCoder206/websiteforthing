s = input("-> ")
con = 0
vow = {'a', 'e', 'i', 'o', 'u'}
for i in s:
    if i.isalpha() and i not in vow:
        con += 1
    if i in vow:
        con = 0
if con >= 4:
    print("Hard to pronounce")
else:
    print("Not hard to pronounce")
