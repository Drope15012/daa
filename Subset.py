f = False

def sub(a, t, s=[], i=0):
    global f
    if t == 0:
        print(s)
        f = True
        return
    for j in range(i, len(a)):
        if a[j] <= t:
            sub(a, t-a[j], s+[a[j]], j+1)

a = list(map(int, input("Elements: ").split()))
t = int(input("Target: "))

sub(a, t)

if not f:
    print("No possible solution")
