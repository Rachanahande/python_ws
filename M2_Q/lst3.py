data = "Rajesh,Krish,manoj,suresh,jayesh,mahesh,charan,avinash"
names= data.upper().split(",")
print(names)
lst=[]
for name in names:
    if name.startswith("A") or name.endswith("H"):
        lst.append(name)
lst.sort()
print(lst)