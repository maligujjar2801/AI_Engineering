def fibocanni(limit):
    a,b = 0,1
    for _ in range(limit):
        yield a
        a,b = b,a+b


for numbers in fibocanni(10):
    print(numbers)