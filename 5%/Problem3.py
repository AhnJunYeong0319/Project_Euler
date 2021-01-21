import math

num = 600851475143
root = math.sqrt(num)
my_list = []

for i in range(2, math.trunc(root)+1):
    if (num % i) == 0:
        my_list.extend([i, num/i])

factors = sorted(my_list)[::-1]

# 소수 판별 함수
def det_prime(factors):
    for i in factors:
        t = 1
        # 소수 판별
        for j in range(2, int(math.sqrt(i)) + 1):
            # x가 해당 수로 나누어 떨어진다면
            if i % j == 0:
                t = 0
                break
        if t == 1:
            break
    return i

print(det_prime(factors))
