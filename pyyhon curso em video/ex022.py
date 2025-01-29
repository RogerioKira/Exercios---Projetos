def f(lst):
    p = 0
    while p < len(lst):
        lst[p] *= 2
        p += 1

v = [5,3,9,1,0,2]
f(v)
print(v)