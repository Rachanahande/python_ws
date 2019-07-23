data="RAJ,SIVA,MANI,sonu,anu,tanvi"
x=list(map(lambda x:x.capitalize(),data.split(",")))
print(list(filter(lambda x:x.startswith("A"),x)))