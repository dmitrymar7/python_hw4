def task3():
    lst = input("Введите последовательность элементов: ").split()
    lst_u = list()
    for i in lst:
        if i in lst_u:
            continue
        lst_u.append(i)
    lst_nr = [i for i in lst if lst.count(i) < 2]
    print(f"Исходный список: {lst}")
    print(f"Список уникальных элементов: {lst_u}")
    print(f"Список неповторяющихся элементов: {lst_nr}")

task3()