def fibonacci(n):
    fib_sequence = [0, 1]
    while True:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        if next_number > n:
            break
        fib_sequence.append(next_number)
    return fib_sequence

n = 4000000  # İstediğiniz sınırı burada belirleyin
fib_sequence = fibonacci(n)
toplam = 0
for i in fib_sequence:
    if i % 2 == 0:
        toplam += i

print(toplam)
