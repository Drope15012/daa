c = 0

def toh(n, s, t, d):
    global c
    if n:
        toh(n-1, s, d, t)
        print(s, "-->", d)
        c += 1
        toh(n-1, t, s, d)

n = int(input("Disks: "))
toh(n, "S", "T", "D")
print("Moves:", c)
