#print(sum([3*(ord(a)==ord(b)-23)+6*((a=="A"and b=="Y")or(a=="B"and b=="Z")or(a=="C"and b=="X"))+(b=='X')+2*(b=='Y')+3*(b=='Z')for a,b in[i.split() for i in open("data2.txt","r").read().split("\n")]]))
s = 0
for a,b in[i.split() for i in open("data2.txt","r").read().split("\n")]:
    s += 3*(ord(b)-88)
    if b == "X":
        s += 1 if a == "B" else 2 if a == "C" else 3
    elif b == "Y":
        s += 1 if a == "A" else 2 if a == "B" else 3
    elif b == "Z":
        s += 1 if a == "C" else 2 if a == "A" else 3


print(s)