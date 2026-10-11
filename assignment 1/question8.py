# Input strings
string1 = "Python"
string2 = "Class"

# Initialize variables
i = 0
result = ""

# Find lengths
len1 = len(string1)
len2 = len(string2)

# Loop until both strings are fully traversed
while i < len1 or i < len2:
    if i < len1:
        result += string1[i]
    if i < len2:
        result += string2[i]
    i += 1

# Output
print("string3 =", result)