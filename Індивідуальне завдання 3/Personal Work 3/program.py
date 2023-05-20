import matplotlib.pyplot as plt
import math

def read_from_file(path):
    with open(path) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
        matrix = [[float(j) for j in i.split(", ")] for i in lines]
    return matrix
def parse_from_text_box(mat_str):
    lines = [i.replace("\n", "") for i in mat_str.split("\n")]
    return lines
def print_matrix(matrix):
    for i in matrix: print(i)
def print_system(lst):
    to_return = ""
    if len(lst) == 6:
        to_return += f"a * {round(lst[0], 3)}  + b * {lst[1]} = {round(lst[2], 3)}"
        to_return += f"\na * {round(lst[3], 3)} + b * {round(lst[4], 3)} = {round(lst[5], 3)}"
    else:
        to_return += f"{round(lst[0], 3)} * a + {lst[1]} * b + {round(lst[2], 3)} * c = {round(lst[3], 3)}"
        to_return += f"\n{round(lst[4], 3)} * a + {lst[5]} * b + {round(lst[6], 3)} * c = {round(lst[7], 3)}"
        to_return += f"\n{round(lst[8], 3)} * a + {lst[9]} * b + {round(lst[10], 3)} * c = {round(lst[11], 3)}"
    return to_return


def get_x_i(matrix):
    return matrix[0][1:]
def get_y_i(matrix):
    return [matrix[i][0] for i in range(1, len(matrix))]
def get_n_i(matrix):
    return [sum([matrix[i][j] for i in range(1, len(matrix))]) for j in range(1, len(matrix[0]))]
def get_m_i(matrix):
    return [sum(matrix[i][1:]) for i in range(1, len(matrix))]


def get_cond_avg(matrix):
    y_i, n_i = get_y_i(matrix), get_n_i(matrix)
    return [sum([y_i[i - 1] * matrix[i][j] for i in range(1, len(matrix))]) / n_i[j - 1] for j in
            range(1, len(matrix[0]))]
def lin_space(start, end, steps):
    step = (end - start) / steps
    return [start + step * i for i in range(steps + 1)]
def draw_plot(x, y, x1, y1):
    plt.scatter(x, y)
    plt.scatter(x1, y1)
    plt.show()


def kramer_method(lst):
    det = lst[0] * lst[4] - lst[3] * lst[1]
    det_a = lst[2] * lst[4] - lst[5] * lst[1]
    det_b = lst[0] * lst[5] - lst[3] * lst[2]
    a = round(det_a / det, 4)
    b = round(det_b / det, 4)
    return [a, b]
def kramer_method_3(lst):
    det = lst[0] * (lst[5] * lst[10] - lst[9] * lst[6]) - lst[4] * (lst[1] * lst[10] - lst[9] * lst[2]) + lst[8] * (lst[1] * lst[6] - lst[5] * lst[2])
    det_a = lst[3] * (lst[5] * lst[10] - lst[9] * lst[6]) - lst[7] * (lst[1] * lst[10] - lst[9] * lst[2]) + lst[11] * (lst[1] * lst[6] - lst[5] * lst[2])
    det_b = lst[0] * (lst[7] * lst[10] - lst[11] * lst[6]) - lst[4] * (lst[3] * lst[10] - lst[11] * lst[2]) + lst[8] * (lst[3] * lst[6] - lst[7] * lst[2])
    det_c = lst[0] * (lst[5] * lst[11] - lst[9] * lst[7]) - lst[4] * (lst[1] * lst[11] - lst[9] * lst[3]) + lst[8] * (lst[1] * lst[7] - lst[5] * lst[3])
    a, b, c = det_a / det, det_b / det, det_c / det

    return [a, b, c]


def solve_parabola_law(matrix):
    x_i, cond_y_i, n_i = get_x_i(matrix), get_cond_avg(matrix), get_n_i(matrix)

    sum_n_i__x_i_4 = sum([n_i[i] * (x_i[i] ** 4) for i in range(len(n_i))])
    sum_n_i__x_i_3 = sum([n_i[i] * (x_i[i] ** 3) for i in range(len(n_i))])
    sum_n_i__x_i_2 = sum([n_i[i] * (x_i[i] ** 2) for i in range(len(n_i))])
    sum_n_i__x_i_1 = sum([n_i[i] * (x_i[i]) for i in range(len(n_i))])

    sum_n_i__y_i__x_i_2 = sum([n_i[i] * cond_y_i[i] * (x_i[i] ** 2) for i in range(len(n_i))])
    sum_n_i__y_i__x_i_1 = sum([n_i[i] * cond_y_i[i] * (x_i[i]) for i in range(len(n_i))])
    sum_n_i__y_i = sum([n_i[i] * cond_y_i[i] for i in range(len(n_i))])

    n = sum(get_n_i(matrix))

    to_return = [sum_n_i__x_i_4, sum_n_i__x_i_3, sum_n_i__x_i_2, sum_n_i__y_i__x_i_2,
                 sum_n_i__x_i_3, sum_n_i__x_i_2, sum_n_i__x_i_1, sum_n_i__y_i__x_i_1,
                 sum_n_i__x_i_2, sum_n_i__x_i_1, n, sum_n_i__y_i]

    system_str = print_system(to_return) + "\na: " + str(round(kramer_method_3(to_return)[0], 3)) \
                 + " b: " + str(round(kramer_method_3(to_return)[1], 3)) \
                 + " c: " + str(round(kramer_method_3(to_return)[2], 3))
    return kramer_method_3(to_return), system_str
def solve_sqrt_law(matrix):
    x_i, cond_y_i, n_i = get_x_i(matrix), get_cond_avg(matrix), get_n_i(matrix)

    sum_n_i_sqrt_x_i = sum([n_i[i] * math.sqrt(x_i[i]) for i in range(len(n_i))])
    n = sum(n_i)
    sum_y_i__n_i = sum([cond_y_i[i] * n_i[i] for i in range(len(n_i))])
    sum_n_i__x_i = sum([n_i[i] * x_i[i] for i in range(len(n_i))])
    sum_n_i__y_i__sqrt_x_i = sum([n_i[i] * cond_y_i[i] * math.sqrt(x_i[i]) for i in range(len(n_i))])

    to_return = [sum_n_i_sqrt_x_i, n, sum_y_i__n_i, sum_n_i__x_i, sum_n_i_sqrt_x_i, sum_n_i__y_i__sqrt_x_i]
    system_str = print_system(to_return) + "\na: " + str(round(kramer_method(to_return)[0], 3)) + " b: " + str(round(kramer_method(to_return)[1], 3))
    return kramer_method(to_return), system_str
def solve_hyper_law(matrix):
    x_i, cond_y_i, n_i = get_x_i(matrix), get_cond_avg(matrix), get_n_i(matrix)

    sum_n_i__1_x_i = sum([1 / (x_i[i]) * n_i[i] for i in range(len(n_i))])
    n = sum(n_i)
    sum_y_i__n_i = sum([cond_y_i[i] * n_i[i] for i in range(len(n_i))])
    sum_n_i__1_x_i_2 = sum([1 / x_i[i] ** 2 * n_i[i] for i in range(len(n_i))])
    sum_n_i__y_i__x_i = sum([n_i[i] * cond_y_i[i] / x_i[i] for i in range(len(n_i))])

    to_return = [sum_n_i__1_x_i, n, sum_y_i__n_i, sum_n_i__1_x_i_2, sum_n_i__1_x_i, sum_n_i__y_i__x_i]
    system_str = print_system(to_return) + "\na: " + str(round(kramer_method(to_return)[0], 3)) + " b: " + str(round(kramer_method(to_return)[1], 3))
    return kramer_method(to_return), system_str
def solve_pow_law(matrix):
    x_i, cond_y_i, n_i, m_i = get_x_i(matrix), get_cond_avg(matrix), get_n_i(matrix), get_m_i(matrix)

    sum_n_i__x_i = sum([n_i[i] * x_i[i] for i in range(len(n_i))])
    n = sum(n_i)
    sum_n_i__lg_y_i = sum([math.log(cond_y_i[i], 10) * n_i[i] for i in range(len(n_i))])
    sum_n_i__x_i_2 = sum([n_i[i] * (x_i[i] ** 2) for i in range(len(n_i))])
    sum_n_i__y_i__sqrt_x_i = sum([n_i[i] * math.log(cond_y_i[i], 10) * x_i[i] for i in range(len(n_i))])

    to_return = [sum_n_i__x_i, n, sum_n_i__lg_y_i, sum_n_i__x_i_2, sum_n_i__x_i, sum_n_i__y_i__sqrt_x_i]
    lg_a, lg_b = kramer_method(to_return)
    system_str = print_system(to_return) + "\na: " + str(round(10**lg_a, 3)) + " b: " + str(round(10**lg_b, 3))

    return [10**lg_a, 10**lg_b], system_str


def f_parabola(x, lst):
    return lst[0] * x**2 + lst[1] * x + lst[2]
def f_sqrt(x, lst):
    return math.sqrt(x) * lst[0] + lst[1]
def f_hyper(x, lst):
    return lst[0] / x + lst[1]
def f_pow(x, lst):
    return lst[0] ** x * lst[1]


def get_sigma(matrix, arr, law):
    x_i, y_i, n_i, m_i, n = get_x_i(matrix), get_y_i(matrix), get_n_i(matrix), get_m_i(matrix), sum(get_n_i(matrix))
    return sum([(y_i[j] - law(x_i[i], arr)) ** 2 * matrix[j + 1][i + 1] for j in range(len(y_i)) for i in
                range(len(x_i))]) / n
def get_delta(matrix, arr, law):
    x_i, y_i, n_i = get_x_i(matrix), get_cond_avg(matrix), get_n_i(matrix)
    return sum([(y_i[i] - law(x_i[i], arr)) ** 2 * n_i[i] for i in range(len(x_i))])



functions = [solve_hyper_law, solve_sqrt_law, solve_pow_law, solve_parabola_law]
dict_of_functions = {solve_hyper_law : f_hyper, solve_sqrt_law : f_sqrt,
                     solve_pow_law : f_pow, solve_parabola_law : f_parabola}

def solve_some_law(law, path):
    matrix = read_from_file(path)
    x_i = get_x_i(matrix)
    y_i = get_cond_avg(matrix)
    y_i_str = "\n".join([str(round(i, 3)) for i in get_cond_avg(matrix)])
    arr, system_str = law(matrix)

    arr = [round(i, 3) for i in arr]
    function_str = ""
    if law == functions[3]:
        function_str = f"{arr[0]}*(x^2) +\n{arr[1]}*x +\n{arr[2]}"
    elif law == functions[2]:
        function_str = f"{arr[0]}^x * {arr[1]}"
    elif law == functions[1]:
        function_str = f"sqrt(x) * {arr[0]} +\n{arr[1]}"
    elif law == functions[0]:
        function_str = f"{arr[0]}/x +\n{arr[1]}"


    arr_x = lin_space(min(x_i) + 0.1, max(x_i) + 1, 1000)
    arr_y = [dict_of_functions[law](x, arr) for x in arr_x]

    return {"sigma" : round(get_sigma(matrix, arr, dict_of_functions[law]), 3),
            "delta" : round(get_delta(matrix, arr, dict_of_functions[law]), 3),
            "system" : system_str,
            "x_i" : x_i,
            "y_i": y_i,
            "y_i_str" : y_i_str,
            "arr_x" : arr_x,
            "arr_y" : arr_y,
            "function" : function_str}