import os

import matplotlib.pyplot as plt

from dataparse import getXY, getColorMap, parseFilename

x = [x for x in range(100)]

files = os.listdir('data')
colors = getColorMap(len(files))
data = {}

for file in files:
    data[parseFilename(file)] = getXY('data/' + file)

plt.figure(figsize=(12, 9))
plt.plot(x, x, linestyle='dashed', color="black")

for i, key in enumerate(data):
    plt.plot(data[key][0], data[key][1], marker='o', linestyle='solid', color=colors(i), label=parseFilename(key))

plt.xticks([5 * x for x in range(20)])
plt.yticks([5 * y for y in range(20)])
plt.ylim(ymin=0, ymax=100)
plt.xlim(xmin=0, xmax=100)
plt.xlabel("Score")
plt.ylabel("Percentile")
plt.title("Exam Percentiles")
plt.grid()
plt.legend(['Standard'] + [parseFilename(key) for key in data])
plt.show()
