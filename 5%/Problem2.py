'''def fibonacci(n):
    fib_list = [1, 1]
    cnt = 2
    while True:
        fib_list.append(fib_list[cnt-1]+fib_list[cnt-2])
        cnt += 1
        if : fib_list[cnt]
            break

    return fib_list'''

import numpy as np

def fibonacci(n):
    fib_list = [1, 2]
    cnt = 1
    while fib_list[cnt] < n:
        fib_list.append(fib_list[cnt] + fib_list[cnt - 1])
        cnt += 1
        if fib_list[cnt] > n:
            fib_list = fib_list[:cnt]
            break

    return fib_list

fib_list = np.array(fibonacci(4000000))
print(sum(fib_list[fib_list%2 == 0]))
