def sum_of_squares(n):
    sum = (n * (n + 1) * (2 * n + 1)) / 6
    return sum

def square_of_sum(n):
    square = ( ((n * (n + 1)) / 2) ) ** 2
    return square

n = int(input("The number is : "))
print(square_of_sum(n) - sum_of_squares(n))