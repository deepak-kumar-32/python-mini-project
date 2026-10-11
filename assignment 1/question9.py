# Pattern printing program

for i in range(1, 6):      # Outer loop for rows
    for j in range(1, i+1):  # Inner loop for numbers
        print(j, end=" ")
    print()  # Move to next line