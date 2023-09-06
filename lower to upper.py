str1 = input("enter the string:")
print("1.upper,2.lower,3.swapcase,4.titile")
n = int(input("select the option:"))
if n == 1:
    print(str1.upper())
elif n == 2:
    print(str1.lower())
elif n == 3:
    print(str1.swapcase())
elif n == 4:
    print(str1.title())
else:
    print("choose the currect option")



#test cases
#1:upper will converts the all letters should be in upper  case and mixed also converts the upper if its empty string then it will be print empty
#2: lower case will convert the string into lower case and mixed alson cinverts the lower case and all should be in alphabetic and empty will gives empty
#3:swapcase will swaps the letters in the given string if its upper then it will cpnvert lower and if its lower then it will convert upper if its mixed then it will swaps and empty string will be give empty
#4:title will gives all letter in the word the first letter should be capital and if its em[pty it will gives empty