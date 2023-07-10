import matplotlib.pyplot as plt


def parseFilename(filename):
    return filename.split('.')[0].replace('-', ' ').capitalize()


def getColorMap(count):
    return plt.cm.get_cmap('gnuplot2', count)


def getXY(filename):
    file = open(filename).read().split('\n')

    columns = len(file[0].split())

    x = []
    y = []

    for c in range(columns):
        for line in file:
            if c < len(line.split()):
                v = line.split()[c]
                if v == '-':
                    continue
                if c % 2 == 0:
                    x.append(int(v))
                else:
                    y.append(int(v))

    return x, y
