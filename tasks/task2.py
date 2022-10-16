
def task2():
    n = int(input("Введите число: "))
    lst = [1]
    lst_simple = []
    i = 2
    while n != 1:
        is_simple = True
        if i not in lst_simple:
            for j in lst_simple:
                if i % j == 0:
                    is_simple = False
                    break

        if not is_simple:
            i += 1
            continue

        if n % i == 0:
            lst.append(i)
            n //= i
        else:
            i += 1

    print(lst)

task2()
