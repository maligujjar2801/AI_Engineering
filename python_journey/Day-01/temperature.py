def temp_converter():
    C=float(input("Enter the temprature in Celcius scale:"))
    F= (C*9/5) + 32
    return f"The temprature in Farenheit scale is {F:.2f}."
print(temp_converter())


