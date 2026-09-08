def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
