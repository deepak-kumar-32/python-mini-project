n = input("Enter a number or word: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")