
def coefs(s: str):
    s = s.replace(" ", "")
    lst_indexes = list()
    index_x = 0

    if s.count("=") != 1:
        raise Exception("Структура выражения не верна")

    dict_coefs = dict()

    index_equals = s.index("=")
    i = 1
    current_str = ""
    current_num = 0
    while index_equals - i > -1:
        if s[index_equals - i].isdigit() or s[index_equals - i] == ".":
            current_str = s[index_equals - i] + current_str
            i += 1
        elif s[index_equals - i] in "x,^":
            current_str = ""
            break
        elif s[index_equals - i] in "+-":
            if s[index_equals - i] == "-":
                current_str = "-" + current_str
            break

    if len(current_str) > 0:
        try:
            current_num = float(current_str)
        except ValueError:
            raise ValueError("Данные в файле некорректны")

    if current_num != 0:
        coef_degree = dict_coefs.get(0, 0)
        dict_coefs[0] = coef_degree + current_num

    while s.count("x", index_x):
        index_x = s.index("x", index_x)
        lst_indexes.append(index_x)
        index_x += 1

    for index_x in lst_indexes:
        current_str = ""
        current_num = 0
        i = 1
        while index_x - i > -1:
            if s[index_x - i].isdigit() or s[index_x - i] == ".":
                current_str = s[index_x - i] + current_str
                i += 1
            else:
                break

        if len(current_str) == 0:
            current_num = 1
        else:
            try:
                current_num = float(current_str)
            except ValueError:
                raise ValueError("Данные в файле некорректны")

        if index_x - i > -1:
            if s[index_x - i] == "-":
                current_num *= -1

        current_str = ""
        current_degree = 1
        i = 1
        if index_x + i < len(s):
            if s[index_x + i] == "^":
                i += 1
                while s[index_x + i].isdigit():
                    current_str += s[index_x + i]
                    i += 1
        if len(current_str) > 0:
            current_degree = int(current_str)
        coef_degree = dict_coefs.get(current_degree, 0)
        dict_coefs[current_degree] = coef_degree + current_num

    return dict_coefs


def text_equation(lst: list):
    k = len(lst) - 1
    text = ""
    for i, value in enumerate(lst):
        if value == 0:
            continue
        sign = "+" if value > 0 else "-"
        degree = k - i

        x = ""
        if degree > 1:
            x = f"x^{degree}"
        elif degree == 1:
            x = "x"

        if len(text) == 0:
            text = f"{abs(value)}"
        else:
            text += f" {sign} {abs(value)}"
        if len(x) > 0:
            text += x

    func_value = 0
    if len(lst) > 0:
        sum_k = sum(lst)
        if sum_k == lst[-1]:
            func_value = lst[-1]

    if len(text) > 0:
        text += f" = {func_value}"

    return text


def task5():
    filename1 = "input1.txt"
    filename2 = "input2.txt"
    str1 = ""
    str2 = ""
    try:
        with open(filename1) as input_file1, open(filename2) as input_file2:
            str1 = input_file1.readline()
            str2 = input_file2.readline()
    except:
        print("Не удалось найти файл")
        return
    d1 = None
    d2 = None

    try:
        d1 = coefs(str1)
    except Exception:
        print("Ошибка разбора уравнения из файла 1")

    try:
        d2 = coefs(str2)
    except Exception:
        print("Ошибка разбора уравнения из файла 2")

    if d1 is None or d2 is None:
        return

    max_coef = max(max(d1.keys()), max(d2.keys()))

    d = {i: d1.get(i, 0) + d2.get(i, 0) for i in range(max_coef + 1)}
    lst = sorted(d.items(), key=lambda x: x[0], reverse=True)
    lst = list(map(lambda x: x[1], lst))

    text = text_equation(lst)
    print(text)

    fileName = "test.txt"
    with open(fileName, "w") as file:
        file.write(text)

task5()