def fib(n):
    if n <= 1:
        return 1
    else:
        number = fib(n-1) + fib(n-2)
        return number

n = 6

for i in range(n):
    print(fib(i))
