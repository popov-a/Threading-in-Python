#https://docs-python.ru/tutorial/mnogopotochnost-python/

import threading as th
import time

my_t = list()

def my_func_2(i, j):
    global  my_t
    my_t.append((i, j))

def my_func(j, n):
    time_start = time.time()
    print(f'Поток {n} стартанул ...')
    sum = 0
    for i in range(30000000):
        sum += i
    my_func_2(j, n)
    print(f'Поток {n} закончил. Время работы {time.time() - time_start}')

if __name__ == '__main__':
    for j in range(1, 4):
        print(f'\nЗапускаем {j} потоков:')
        t = list()
        for i in range(j):
            t.append(th.Thread(target=my_func, args=(j, i)))
            t[i].start()
        for i in range(j):
            t[i].join()

    print(f'\nДоступ к глобальным переменным {my_t}')