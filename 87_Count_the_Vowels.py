def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in string:
        if ch in vowels:
            count += 1

    return count

# Input a string
text = input("Enter a string: ")

# Call the function
result = count_vowels(text)

print("Number of vowels:", result)