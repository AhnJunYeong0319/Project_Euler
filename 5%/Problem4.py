A, B, C = 0, 0, 0

for a in range(9, 0, -1):
    for b in range(9, -1, -1):
        for c in range(9, -1, -1):
            checker = 9091 * a + 910 * b + 100 * c
            i = 90
            while True:
                if ((checker % i) == 0) & (100 <= (checker // i) <= 999):
                    A, B, C = a, b, c
                    break
                else:
                    i -= 1
                    if i == 9:
                        A, B, C = a, b, c
                        break
                    else:
                        continue
            if i != 9:
                break
            else:
                continue
        if i != 9:
            break
        else:
            continue
    if i != 9:
        break
    else:
        continue

print(A, B, C)
print(f"The largest palindrom number for Prob. 4: {checker*11}")




