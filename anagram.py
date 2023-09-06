string1 = input("enter a streing")
string2 = input("enter a string")
if len(string1) != len(string2):
     print("not a anagram")
else:
    if sorted(string1) == sorted(string2):
        print("it's a anagram")
    else:
        print("not a anagram")

#test cases
#1:basic algarithms
##2:different length will occur it will be false
#3:case sensitivity when its upper or lower  case does not matter
#4:white spaces handling
#5:non alpha numeric
#6:empty string we will give and that will be a anagram
#7:single character strings like a  and a
#8:large inputs will taken while its getting same length or not
#9:unicode characters will also one test case for anagram
