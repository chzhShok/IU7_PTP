import glob
import os
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
from sys import argv

try:
    flag = argv[1]
except IndexError:
    print('Enter flag to draw graphs')
    print('1 - ordinary graph of function')
    print('2 - graph of function with max values and min values')
    print('3 - graph of function with boxplots')
    flag = '0'

colors: list[str] = list(TABLEAU_COLORS.values())
figure_width: int = 12
figure_height: int = 7

preproc_path: str = 'preproc_data'
data_path: str = 'data'

preproc_files: list[str] = glob.glob(os.path.join(preproc_path, '*.txt'))
data_files: list[str] = glob.glob(os.path.join(data_path, '*.txt'))

# Обычный кусочно-линейный график
if flag == '1':
    plt.figure(figsize=(figure_width, figure_height))
    plt.title('Ordinary graph of function')
    plt.xticks(rotation=90)
    plt.xlabel('N')
    plt.ylabel('Avg')
    for file in preproc_files:
        with open(file, 'r') as f:
            f.readline()
            x: list[int] = []
            y: list[float] = []
            for line in f.readlines():
                n, avg = int(line.split()[0]), float(line.split()[1])
                x.append(n)
                y.append(avg)

            plt.plot(x, y, marker='o', label=file)

    plt.legend()

# Кусочно-линейный график с ошибкой
if flag == '2':
    plt.figure(figsize=(figure_width, figure_height))
    plt.title('Graph of function with max values and min values')
    plt.xticks(rotation=90)
    plt.xlabel('N')
    plt.ylabel('Avg')
    count = 0
    for file in preproc_files:
        color = colors[count % len(colors)]
        with open(file, 'r') as f:
            f.readline()
            x: list[int] = []
            y: list[float] = []
            maxes: list[float] = []
            minis: list[float] = []
            for line in f.readlines():
                n, avg = int(line.split()[0]), float(line.split()[1])
                maxi, mini = float(line.split()[3]), float(line.split()[4])
                x.append(n)
                y.append(avg)
                maxes.append(maxi)
                minis.append(mini)

            for i in range(len(maxes)):
                plt.plot([x[i], x[i]], [maxes[i], minis[i]], color=color)

            plt.scatter(x, maxes, marker='_', color=color)
            plt.scatter(x, minis, marker='_', color=color)
            plt.plot(x, y, marker='o', label=file, color=color)

        count += 1

    plt.legend()

# График с усами
if flag == '3':
    count: int = 0
    fig, ax = plt.subplots(sharex='all', sharey='all', figsize=(figure_width, figure_height))
    ax.set_title("Graph of function with boxplots")
    ax.set_xlabel('N')
    ax.set_ylabel('Time')
    for file in data_files:
        color: str = colors[count % len(colors)]
        with open(file, 'r') as f:
            data: list[list[int | float]] = [[int(line.split()[0]), float(line.split()[1])] for line in f.readlines()]
            result_dict: dict[int, list[float]] = {}
            # Проходим по массиву и заполняем словарь
            for item in data:
                key = item[0]
                value = item[1]
                if key in result_dict:
                    result_dict[key].append(value)
                else:
                    result_dict[key] = [value]

            result_dict = dict(sorted(result_dict.items()))

            maxes: list[float] = [max(value) for value in result_dict.values()]
            minis: list[float] = [min(value) for value in result_dict.values()]
            avg: list[float] = [sum(value)/len(value) for value in result_dict.values()]
            ns: list[int] = list(result_dict.keys())

            for i in range(len(maxes)):
                plt.plot([ns[i], ns[i]], [maxes[i], minis[i]], color=color)

            plt.scatter(ns, maxes, marker='_', color=color)
            plt.scatter(ns, minis, marker='_', color=color)
            plt.plot(ns, avg, marker='o', label=file, color=color)

            for key, value in result_dict.items():
                ax.boxplot(value, positions=[key], widths=50)

            plt.xticks(rotation=90)

        count += 1

    plt.legend()

plt.show()
