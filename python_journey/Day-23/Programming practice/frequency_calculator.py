def frequency_calculator(sentance):
    frequency = {}
   
    words = sentance.split()
    
    for word in words:
        if word in frequency.keys():
            frequency[word] += 1
        else :
            frequency[word] = 1

    for word , n in frequency.items():
        print(f"Word: {word}\tFrequency: {n}")

if __name__ == "__main__":

    sentance = input("Enter any sentance :")
    frequency_calculator(sentance)