import random

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

def task4():
    k = int(input("Введите натуральную степень: "))
    lst = [random.randint(0, 100) for i in range(k + 1)]
    text = text_equation(lst)

    print(f"Коэффициенты {lst}")
    print(text)

    fileName = "test.txt"
    with open(fileName, "w") as file:
        file.write(text)


task4()