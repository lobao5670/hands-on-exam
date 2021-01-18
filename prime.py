def prime(n):
    if n < 2:
        print('not prime')
    else:
        for i in range(2, n):
            if (n % i) == 0:
                print('not prime')
                break
        if i == n-1:
            print('prime')

prime(20)