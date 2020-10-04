def generator(n):
    a = 1
    while a <= n:
        if a % 3 == 0:
            yield 'Василий'
            a += 1
        yield a
        a += 1

a = generator(7)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
