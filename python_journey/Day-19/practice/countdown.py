def countdown():
    for n in range(10,0,-1):
        yield n

for number in countdown():
    print(number)