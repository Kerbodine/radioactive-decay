import random
import matplotlib.pyplot as plt

init_count = 100000
iter = 20

iterations = 0

count = init_count
temp_count = count

x = []
y = []

for i in range(iter):
    iterations += 1
    for i in range(count):
        num = random.randint(1, 6)
        if num == 1:
            temp_count -= 1
    print(
        f"Current count: {temp_count}/{init_count} ({round((temp_count / init_count) * 100, 3)}%)\n")
    y.append(temp_count)
    x.append(iterations)
    count = temp_count

print(x)
print(y)

fig, ax = plt.subplots(1)

plt.title(f"Nuclear Decay Plots\n{init_count} particles, {iter} iterations")
plt.xlabel('Iterations')
plt.ylabel('Particles remaining')

plt.scatter(x, y)
plt.plot(x, y, marker='.', markersize=10)
plt.show()

ax.plot(x, y)
