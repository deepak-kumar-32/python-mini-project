# Input string
s = "ABBCDABBEEFFBCDA"

# Empty list to store unique characters
result = []

# Loop through each character
for ch in s:
    if ch not in result:
        result.append(ch)

# Convert list back to string
output = "".join(result)

# Print result
print(output)