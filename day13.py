from functools import cmp_to_key

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

        if q != 2: return q
    
    #print("All equal until now", len(b) == len(a), len(b) > len(a))

    return 2 if len(b) == len(a) else len(b) > len(a)

c,d = [[2]],[[6]]

packets = [c,d]

for a, b in data:
    packets.append(a)
    packets.append(b)



def partition(A, lo, hi):
    pivot = A[hi]

    i = lo - 1

    for j in range(lo, hi):
        if lteq(A[j], pivot):
            i = i + 1
            A[j], A[i] = A[i], A[j]
    
    i += 1
    A[hi], A[i] = A[i], A[hi]
    return i

def quicksort(A, lo, hi):
    if lo >= hi or lo < 0: 
        return
    p = partition(A, lo, hi)
    quicksort(A, lo, p - 1)
    quicksort(A, p + 1, hi)

quicksort(packets, 0, len(packets) - 1)
    
print((packets.index(c)+1)*(packets.index(d)+1))