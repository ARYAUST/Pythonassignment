text ="programming"
freq ={}
for char in text:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] =1

        print("Character Frequency:")
        for char, count in freq.items():
            print(char, ":", count)