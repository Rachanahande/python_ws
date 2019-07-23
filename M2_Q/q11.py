C = ["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
F = ["PKM","ALN","RMZ","CS","MCS"]
B = ["PKM","ALN","NV","KM","RMV"]
players=[]
players.extend(C)
players.extend(F)
players.extend(B)
u_name = []
for name in players:
    if name in u_name:

    else:
        u_name.append(name)
print(u_name)
