string = "Hello World!"
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Vowel Count:",count)




string = "madamr"
is_palindrome = True
for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 12
print("The factorial of", num, "is", factorial(num))
