import time
import matplotlib.pyplot as plt

def quick(a):
    if len(a) <= 1: return a
    p = a[0]
    return quick([x for x in a[1:] if x <= p]) + [p] + quick([x for x in a[1:] if x > p])

n, t = [], []

for _ in range(int(input("Tests: "))):
    s = int(input("Elements: "))
    a = list(map(int, input().split()))

    st = time.time()
    a = quick(a)
    en = time.time()

    print("Sorted:", a)
    n.append(s)
    t.append(en - st)

plt.plot(n, t, "o-")
plt.xlabel("n")
plt.ylabel("Time")
plt.grid()
plt.show()
