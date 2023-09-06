string = input("enter a string:")
string_1 = len(string)           #taking string length assign to new variable string_1
for row in range(string_1):      #iterating the row value in the length of the string
    for col in range(row+1):     #iterating the column value in the row postion to +1 it means end
        print(string[col],end="") #here print will print the column and and it converted into string  and end will keeps the line as usual
    print()                       #orint used for the new row in the program


#test cases
#1: *
#2: numbers
#3:alphabetic
#4:same number in same row like 1
                         #      22
                         #      333
