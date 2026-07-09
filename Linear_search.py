import time
import matplotlib.pyplot as plt

def linear(a, k):
    for i, x in enumerate(a):
        if x == k:
            return i
    return -1

n, t = [], []

for _ in range(int(input("Experiments: "))):
    size = int(input("No. of elements: "))
    a = list(map(int, input("Elements: ").split()))
    key = int(input("Search element: "))

    s = time.time()
    p = linear(a, key)
    e = time.time()

    n.append(size)
    t.append(e - s)

    print("Found at", p + 1 if p != -1 else "Not Found")
    print("Time:", e - s)

plt.plot(n, t, "o-")
plt.xlabel("n")
plt.ylabel("Time")
plt.grid()
plt.show()
