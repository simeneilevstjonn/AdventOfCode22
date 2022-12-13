data = [[eval(i.split("\n")[0]), eval(i.split("\n")[1])] for i in open("data13.txt","r").read().split("\n\n")]

def lteq(a, b):
    for i in range(min(len(a), len(b))):
        # Both integers
        if type(a[i]) == type(0) and type(b[i]) == type(0):
            if a[i] < b[i]:
                return True
            elif a[i] < b[i]:
                return False
            continue
        # One integer
        if type(a[i]) == type(0) and type(b[i]) == type([]):
            a[i] = [a[i]]
        elif type(a[i]) == type([]) and type(b[i]) == type(0):
            b[i] = [b[i]]
        
        if (q:=lteq(a[i], b[i])) is not None: return q
    
    return None if len(b) == len(a) else len(b) > len(a)

i = 1
s = 0
for a, b in data:
    if lteq(a, b):
        print(i)
        s += i
    i += 1

print(s)
