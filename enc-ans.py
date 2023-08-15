# Write a function which generates a random integer from a given range without using the random lib (Q1)
from time import time_ns
def ranint(least:int,most:int) -> int:
    rn = time_ns()
    last = rn % 1000
    rint = least + (last * (most - least + 1) // 1000)
    return rint
# Given an array of 9 integers convert ints to the corresponding strings and print them in form of 3x3 grid (Q9)
def num_to_str(arr:list) -> None:
    syms = {0:"space",1:"X",2:"O"}
    for ind,ele in enumerate(arr):
        print(syms.get(ele), end="\t")
        if ind % 3 == 2: print()
# Number-Alphabet decoding (Q5)
def num_alph(s:str) -> None:
    alphs = {str(i): chr(i + 96) for i in range(1,26 + 1)}
    finstr = ""
    for i in range(0,len(s),2):
        if i+2 < len(s):
            finstr += alphs.get(s[i:i+2])
    print(finstr)
    return
# Target sum (Q7)
def targ_sum(arr:list[int],targ:int) -> None:
    arr.sort()
    l,r = 0,len(arr) - 1
    while l < r:
        currs = arr[l] + arr[r]
        if currs == targ: print(f"{arr[l]} and {arr[r]} sum up to {targ}"); return
        elif currs < targ: l += 1
        else: r -= 1
    print(f"No two elements sum up to {targ}")
# Dudeney numbers (Q8)
from math import cbrt
def ddney(mi:int,mx:int) -> tuple:
    def digitsum(num:int):
        return sum(map(int,str(num)))
    check = lambda x: float(digitsum(x)) == cbrt(x)
    nums = tuple(filter(check,[n for n in range(mi,mx+1)]))
    return nums
print(ddney(1,10000))
# Hard to pronounce (Q10)
def htp(s:str) -> bool:
    coun = 0
    vows = ("a","e","i","o","u")
    for c in s:
        if c not in vows: coun += 1
        else: coun = 0
    return coun >= 4
# Matrix search (Q4)
def matrix_search(mat:list,targ) -> bool:
    m,n = len(mat),len(mat[0])
    l,r = 0,m * n - 1
    while l <= r:
        mid = (l+r) // 2
        mid_val = mat[mid // n][mid % n]
        if mid_val == targ: return True
        elif mid_val < targ: l = mid + 1
        else: r = mid - 1
    return False
# Second largest element (Q6)
def largest(arr:list[int],n:int = 2) -> int:
    assert n > 0 and n <= len(arr)
    def sort(arr:list[int]) -> list[int]:
        for i in range(1,len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    return sort(arr)[len(arr) - n]
