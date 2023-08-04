#Que 1 Prime Numbers
def ifprime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

primeNumbers = []

for num in range(2, 51):
    if ifprime(num):
        primeNumbers.append(num)

print(primeNumbers)

#Que2 Table
number = int(input('Enter a number '))

for i in range(1, 11):
   print(number, '*', i, '=', number*i)

#Que3 Palindrome String
def isPalindrome(s):
	return s == s[::-1]

s=input('Enter a string ')
ans = isPalindrome(s)

if ans:
	print("Palindrome")
else:
	print("Not a Palindrome")


#Que4 Reverse a String
def revString(input_string):
    return input_string[::-1]


input_string = input("Enter a string: ")
reversed = revString(input_string)

print("Reversed string:", reversed)






