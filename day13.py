data = [[eval(i.split("\n")[0]), eval(i.split("\n")[1])] for i in open("data13.txt","r").read().split("\n\n")]

def lteq(a, b):
    for i in range(min(len(a), len(b))):
        #print("comparing", a[i], b[i])
        # Both integers
        if type(a[i]) == type(0) and type(b[i]) == type(0):
            if a[i] < b[i]:
                #print("returning true")
                return True
            elif a[i] > b[i]:
                #print("returning false")
                return False
            #print("equal")
            continue
        # One integer
        if type(a[i]) == type(0) and type(b[i]) == type([]):
            #print("wrapping a in list")
            a[i] = [a[i]]
        elif type(a[i]) == type([]) and type(b[i]) == type(0):
            #print("wrapping b in list")
            b[i] = [b[i]]
        
        q=lteq(a[i], b[i])

        #print("Listcomp", q)

        if q is not None: return q
    
    #print("All equal until now", len(b) == len(a), len(b) > len(a))

    return None if len(b) == len(a) else len(b) > len(a)

i = 1
s = 0
for a, b in data:
    #print("Start compare of pair",i)
    if lteq(a, b):
        #print(i)
        s += i
    i += 1

print(s)
