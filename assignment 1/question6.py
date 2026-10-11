# Input string
original_string = "Learning Python is easy."

# Remove the period if you want to keep the word "easy" clean, 
# or keep it as part of the word.
# Splitting the string into a list of words
words = original_string.split()

# Initializing variables
reversed_words = []
index = len(words) - 1

# Using a while loop to iterate backwards
while index >= 0:
    reversed_words.append(words[index])
    index -= 1

# Joining the words back into a single string
output_string = " ".join(reversed_words)

print("Input: ", original_string)
print("Output:", output_string) 