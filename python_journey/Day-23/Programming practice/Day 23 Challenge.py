from frequency_calculator import frequency_calculator


sentance = input("Enter any sentance :")
words = sentance.split()

total_length = len(words)
print("Total Words : ",total_length)

unique = set(words)
print("Unique Words :",end="")
for word in unique:
    print(word,end = ",")
print("\n")
frequency_calculator(sentance)


