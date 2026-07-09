import random, time
import matplotlib.pyplot as plt

def sel(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

n = [10, 20, 30, 40, 50]
t = []

for i in n:
    a = [random.randint(1, 100) for _ in range(i)]
    s = time.time()
    sel(a)
    t.append(time.time() - s)

plt.plot(n, t, "o-")
plt.xlabel("n")
plt.ylabel("Time")
plt.grid()
plt.show()
