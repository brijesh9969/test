import matplotlib.pyplot as plt
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
theta = [0, 1, 2.5]
r = [0, 0.1, 0.2]
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
plt.show()
# plt.savefig("out.png")
