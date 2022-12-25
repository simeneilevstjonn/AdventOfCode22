def parseSNAFU(s):
    n = 0
    digits = {"0" : 0, "1": 1, "2": 2, "-" : -1, "=" : -2}

    for i, d in enumerate(s):
        n += digits[d] * 5 ** (len(s) - 1 - i)

    return n

number = sum(parseSNAFU(i) for i in open("data25.txt", "r").read().split("\n"))

def decimalToSNAFU(n):
    s = ""

    while n != 0:
        d = n % 5
        carry = 0

        if d < 3:
            s = str(d) + s
        elif d == 3:
            s = "=" + s
            carry = 1
        elif d == 4:
            s = "-" + s
            carry = 1

        n //= 5
        n += carry

    return s

print(decimalToSNAFU(number))



