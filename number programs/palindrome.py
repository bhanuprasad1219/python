string = input("enter a string:")
rev_string = string[::-1]
if string == rev_string:
    print("it's a palindrome")
else:
    print("not a palindrom")


#test cases
#1:madam is palindrome its reeds the left to right and right to left as same as a string
#2: 1221 its also a palindrome  its also reeds and getting same output
#3:a man, a plan,a canal, panama in this the punctuation marks and spaces  will be ignored
#4: teacher is not a palindrome