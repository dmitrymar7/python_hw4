
#В задаче релизуем несколько алгоритмов вычисления числа pi с отображением временя для возможности
#сравнения эффективности

import random
import time
from pprint import pprint
import math

def round_d(num: float, d:float):
    str_d = str(d)
    if str_d.count(".") == 0:
        return round_d(num)
    ndigits = len(str_d[str_d.index("."):])
    return round(num, ndigits)

def decorator(algorithm):
    def pi_time(func):
        def wrap(*arg, **keywords):
            t = time.time()
            p = func(*arg)
            t = time.time() - t
            t = round(t, 2)
            d = arg[0]
            d = {"result": round_d(p, d), "time": t, "algorithm": algorithm}
            return d
        return wrap
    return pi_time


#Ряд Грегори–Лейбница
@decorator("Ряд Грегори–Лейбница")
def pi_Gregory_Leibniz(d):
    n = 1000000
    p = 0
    for i in range(n):
        current_pi = p + 4 * math.pow(-1, i) / (2 * i + 1)
        if abs(p - current_pi) < d:
            p = current_pi
            break
        p = current_pi
    return p

@decorator("Метод Монте-Карло")
def pi_montecarlo(d):
    #Зададим окружность радиусом 1 с ценром в точек 0, 0
    #Sкруга = pi*(r^2)
    #Sвнешнего квадрата 4*(r^2)
    #pi = Sкруга/Sвнешнего квадрата * 4
    rad = 1
    n = 10000000
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= rad ** 2:
            count += 1
    s_square = 4 * (rad ** 2)
    s_circle = count * s_square / n
    p = s_circle * 4 / s_square
    return p

@decorator("Формула Эйлера")
def pi_euler(d):
    n = 1000000
    p = 0
    for i in range(n):
        p = p + 1 / math.pow(i + 1, 2)
    p = math.sqrt(6 * p)
    return p

def task1():

    d = 0.0001

    dct = pi_montecarlo(d)
    pprint(dct)

    dct =pi_Gregory_Leibniz(d)
    pprint(dct)

    dct = pi_euler(d)
    pprint(dct)

task1()