scores =[[1,2,3,4],[4,5,6,7],[6,7,8,9]]
res=0
for score in scores:
    for s in score:
        res += s
print(f"result {res}")