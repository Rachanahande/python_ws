name=input("enter your name:")
lst = ['a','e','i','o','u']
lst.append("python")
print((len(list(filter(lambda x: x in lst,name)))))
print(lst)