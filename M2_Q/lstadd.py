lst1 = [1,2,3,4]
lst2 = [4,5,6,7]
res = []
for i in range(len(lst1)):
    res.append(lst1[i]+lst2[i])
print(res)

''' res= list(map(lambda a,b :a+b,lst1,lst2))'''