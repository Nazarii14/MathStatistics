import matplotlib.pyplot as plt
import math
from scipy import integrate
from scipy.stats import chi2

def sum_(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return round(result, 6)
get_midpoint = lambda tpl: (tpl[0] + tpl[1]) / 2
def average_(intervals, counts):
    result = 0
    for i in range(len(intervals)):
        result += get_midpoint(intervals[i]) * counts[i]
    return result / sum_(counts)
def deviation_(lst, counts):
    to_return = 0
    avg = average_(lst, counts)
    for i in range(len(lst)):
        to_return += (((get_midpoint(lst[i]) - avg) ** 2) * counts[i])
    return to_return
dispersion_ = lambda lst, counts: deviation_(lst, counts) / sum_(counts)
round4 = lambda x: round(x, 4)
def F(x):
    integrand = lambda t: math.exp(-t ** 2 / 2)
    return round4(1 / math.sqrt(2 * math.pi) * integrate.quad(integrand, 0, x)[0])
def xi2_emp(counts, n_prob):
    res = 0
    for i in range(len(counts)):
        res += (counts[i] - n_prob[i]) ** 2 / n_prob[i]
    return res
def xi2_cr(alpha, df):
    with open("xi2_critical.txt", 'r') as f:
        lines = f.readlines()
        return float(lines[int((df-1)*999+(alpha-0.001)*1000)])

def show_plot_normal(intervals, counts):
    plt.plot([intervals[0][0], intervals[-1][1]], [0, 0])
    for i in range(len(intervals)):
       s, e = intervals[i]
       plt.plot([s, s], [0, counts[i]], color='black')
       plt.plot([s, e], [counts[i], counts[i]], color='black')
       plt.plot([e, e], [0, counts[i]], color='black')
    plt.show()
def show_plot_even(numbers, counts):
    plt.plot(numbers, counts)
    plt.show()
def print_table(numbers, counts, probs, n_probs):
    str = ""
    for i in range(len(numbers)):
        if type(numbers[i]) == int:
            str += f'\n{round4(numbers[i])} | {counts[i]} | {round4(probs[i])} | {round4(n_probs[i])}'
        else:
            str += f'\n{round4(numbers[i][0])} - {round4(numbers[i][1])} | {counts[i]} | {round4(probs[i])} | {round4(n_probs[i])}'
    return str
def countElementsIntervals(numbers, inters, counts):
    result = []
    for i in inters:
        counter = 0
        for x in range(len(numbers)):
            if i == inters[0]:
                if i[0] <= numbers[x] <= i[1]:
                    counter += counts[x]
            else:
                if i[0] < numbers[x] <= i[1]:
                    counter += counts[x]
        result.append(counter)
    return result


with open("xi2_critical.txt", 'r') as f:
    lines = f.readlines()
    print(str(lines.index("5.991464547107979\n")))

# Задача 1
def normalLaw(intervals=[], counts=[], a=-1, sigma=-1, alpha=-1):
    if intervals == [] and counts == []:
        with open('Data.txt', 'r') as f:
            lines = f.readlines()
            counts = [int(x) for x in lines[1].strip().split(', ')]
            intervals = [(float(x.split('-')[0]), float(x.split('-')[1])) for x in lines[0].strip().split(', ')]

    str_ = 'Задача 1\n\nГіпотеза: H0 - нормальний закон розподілу'

    if a == -1:
        a = average_(intervals, counts)
    if sigma == -1:
        sigma = math.sqrt(dispersion_(intervals, counts))
    if alpha == -1:
        alpha = 0.05

    str_ += "\n\na: " + str(round4(a))
    str_ += "\nsigma: " + str(round4(sigma))
    str_ += "\nalpha: " + str(round4(alpha))

    probabilities = [round4(0.5 + F((intervals[0][1] - a) / sigma))]

    for i in range(1, len(intervals) - 1):
        probabilities.append(round4(F((intervals[i][1] - a) / sigma) - F((intervals[i][0] - a) / sigma)))

    probabilities.append(round4(1 - sum_(probabilities)))
    n_probabilities = [round4(sum_(counts) * x) for x in probabilities]
    print(probabilities)

    invalid_indices = [i for i in range(len(intervals)) if counts[i] < 5 or n_probabilities[i] < 10]
    str_ += '\n\nІнтервал | Ni | Pi | NPi'
    str_ += print_table(intervals, counts, probabilities, n_probabilities)
    table_is_valid = len(invalid_indices) == 0
    str_ += ('\n\nУмови виконуються\n' if table_is_valid else '\n\nУмови НЕ виконуються\n')

    while not len(invalid_indices) == 0:
        bi = invalid_indices[0]
        new_intervals, new_counts, new_probs, new_n_probs = [], [], [], []

        if bi == len(intervals) - 1:
            bi -= 1

        for i in range(bi):
            new_intervals.append((intervals[i][0], intervals[i][1]))
            new_counts.append(counts[i])
            new_probs.append(probabilities[i])
            new_n_probs.append(n_probabilities[i])

        new_intervals.append((intervals[bi][0], intervals[bi + 1][1]))
        new_counts.append(counts[bi] + counts[bi + 1])
        new_probs.append(probabilities[bi] + probabilities[bi + 1])
        new_n_probs.append(n_probabilities[bi] + n_probabilities[bi + 1])

        for i in range(bi + 2, len(intervals)):
            new_intervals.append((intervals[i][0], intervals[i][1]))
            new_counts.append(counts[i])
            new_probs.append(probabilities[i])
            new_n_probs.append(n_probabilities[i])
        intervals, counts, probabilities, n_probabilities, invalid_indices = new_intervals, new_counts, new_probs, new_n_probs, []

        for i in range(len(intervals)):
            if counts[i] < 5 or n_probabilities[i] < 10:
                invalid_indices.append(i)

    if not table_is_valid:
        str_ += ('\nВалідна таблиця\nІнтервал  | Ni | Pi | NPi')
        str_ += print_table(intervals, counts, probabilities, n_probabilities)

    df = len(intervals) - 2 - 1
    XiE, XiC = xi2_emp(counts, n_probabilities), xi2_cr(alpha, df)

    str_ += (f'\n\nXi^2 емпіричне = {round4(XiE)}\nXi^2 критичне = {round4(XiC)}')
    str_ += ('\n\nxi^2 емп. >= xi^2 крит., тому H0 відхиляємо' if XiE >= XiC else '\n\nxi^2 емп. < xi^2 крит., тому H0 приймаємо')
    return str_

# Задача 2
def evenLaw(numbers=[], counts=[], a_=-1, b_=-1, alpha=0.05):
    if numbers == [] and counts == []:
        with open('Data2.txt', 'r') as f:
            lines = f.readlines()
            numbers = [float(x) for x in lines[0].strip().split(', ')]
            counts = [int(x) for x in lines[1].strip().split(', ')]


    n = math.ceil(1 + math.log(len(numbers), 2))
    h = (numbers[-1] - numbers[0]) / n
    intervals = []
    first = numbers[0]
    for i in range(n):
        intervals.append((first + i * h, first + (i + 1) * h))
    counts_of_intervals = countElementsIntervals(numbers, intervals, counts)

    str_ = "Задача 2\n\nГіпотеза: H0 - рівномірний закон розподілу\n\n"

    avg = average_(intervals, counts_of_intervals)
    sigma = math.sqrt(dispersion_(intervals, counts_of_intervals))
    a = avg - math.sqrt(3) * sigma if a_ == -1 else a_
    b = avg + math.sqrt(3) * sigma if b_ == -1 else b_

    str_ += "a: " + str(round4(a))
    str_ += "\nb: " + str(round4(b))
    str_ += "\nsigma: " + str(round4(sigma))
    str_ += "\nalpha: " + str(round4(alpha))

    probs = [round4((intervals[i][1] - intervals[i][0])/(b-a)) for i in range(len(intervals)-1)]
    probs.append(1-sum_(probs))

    n_probs = [round4(i * sum_(counts_of_intervals)) for i in probs]

    invalid_indices = [i for i in range(len(counts_of_intervals)) if counts_of_intervals[i] < 5 or n_probs[i] < 10]
    str_ += '\n\nІнтервал| Ni | Pi | NPi'
    str_ += print_table(intervals, counts_of_intervals, probs, n_probs)
    table_is_valid = len(invalid_indices) == 0
    str_ += ('\n\nУмови виконуються' if table_is_valid else '\n\nУмови НЕ виконуються')

    #shrink table
    while not len(invalid_indices) == 0:
        bi = invalid_indices[0]
        new_intervals, new_counts, new_probs, new_n_probs = [], [], [], []

        if bi == len(intervals) - 1:
            bi -= 1

        for i in range(bi):
            new_intervals.append((intervals[i][0], intervals[i][1]))
            new_counts.append(counts_of_intervals[i])
            new_probs.append(probs[i])
            new_n_probs.append(n_probs[i])

        new_intervals.append((intervals[bi][0], intervals[bi + 1][1]))
        new_counts.append(counts_of_intervals[bi] + counts_of_intervals[bi + 1])
        new_probs.append(probs[bi] + probs[bi + 1])
        new_n_probs.append(n_probs[bi] + n_probs[bi + 1])

        for i in range(bi + 2, len(intervals)):
            new_intervals.append((intervals[i][0], intervals[i][1]))
            new_counts.append(counts_of_intervals[i])
            new_probs.append(probs[i])
            new_n_probs.append(n_probs[i])
        intervals, counts_of_intervals, probs, n_probs, invalid_indices = new_intervals, new_counts, new_probs, new_n_probs, []

        for i in range(len(intervals)):
            if counts_of_intervals[i] < 5 or n_probs[i] < 10:
                invalid_indices.append(i)

    if not table_is_valid:
        str_ += '\nВалідна таблиця\nЗначення  | Ni | Pi | NPi'
        str_ += print_table(intervals, counts_of_intervals, probs, n_probs)

    df2 = len(intervals) - 2 - 1
    Xi2E_2, Xi2C_2 = xi2_emp(counts_of_intervals, n_probs), xi2_cr(alpha, df2)
    str_ += f'\nXi^2 емпіричне = {round4(Xi2E_2)}' + f'\nXi^2 критичне = {round4(Xi2C_2)}'
    str_ += '\nXi^2 емпіричне >= Xi^2 критичне, \nотже гіпотезу H0 відхиляємо' if Xi2E_2 >= Xi2C_2 else '\nXi^2 емпіричне < Xi^2 критичне, \nотже гіпотезу H0 приймаємо'
    return str_
