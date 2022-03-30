def get_better_way(start, des, limit_len): 
    better = 0
    a = abs(des-start)
    b = start + (limit_len - des)
    return a if a < b else b

print(get_better_way(2, 7, 8))

a =[1,2,4]
b = a.copy()
b.remove(2)
print(a)
print(b)

print([1,4] in a)

a = '34563'
print(list(a))
print(a.split(''))