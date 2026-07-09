import time
import matplotlib.pyplot as plt

def binary(a, k):
    l, h = 0, len(a)-1
    while l <= h:
        m = (l+h)//2
        if a[m] == k: return m
        if a[m] < k: l = m+1
        else: h = m-1
    return -1

n, t = [], []

for _ in range(int(input("Experiments: "))):
    s = int(input("No. of elements: "))
    a = sorted(list(map(int, input("Elements: ").split())))
    k = int(input("Search: "))

    st = time.time()
    p = binary(a, k)
    en = time.time()

    n.append(s)
    t.append(en-st)

    print("Found at", p+1 if p != -1 else "Not Found")
    print("Time:", en-st)

plt.plot(n, t, "o-")
plt.xlabel("n")
plt.ylabel("Time")
plt.grid()
plt.show()
