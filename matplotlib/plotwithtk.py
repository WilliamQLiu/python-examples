import matplotlib.pyplot as plt

plt.ion()
plt.figure()
for i in range(10):
    plt.plot([i], [i], 'o')
    plt.draw()
