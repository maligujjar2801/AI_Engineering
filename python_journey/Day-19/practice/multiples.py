def multiples(n,i):
    def multiply():
        for c in range(1,i+1):
            yield n *c
    return multiply()

for multiple in multiples(7,5):
    print(multiple)