#capitalise
str1 = "hello bhanuprasad"     #the capitalize function will tell the first in the total sentence will be modify as capital.
str1 = str1.capitalize()
print(str1)
str2 = "Hello bhanuprasad"       #if it capital it dont change as small it will remains capital.
str2 = str2.capitalize()
print(str2)

#count                           #the count function will describes the how many of variable or words in the given sentence it will counted and give as output.
str = """Hello Bhanuprasad       
           hkkll"""
str=str.count("l")
print(str)

#endswith                        #endswith describes the last element endswith what  it will desribes it gives as true or false.
str3 = "Hello bhanuprasad"
str3 = str3.endswith("d")
print(str3)

#find function
m = "Hello bhanuprasad"
#m = m.find("p")               #find function will do the finding the index of the word start in a sentence.
#m = m.find("bhanuprasad")
m = m.find("as")
print(m)

#length function            #length is used for finding the length of the sentence.
a = "Hello bhanuprasad"
print(len(a))

#split function
x = "Hello bhanuprasad"
#x = x.split()            # it will separate the words by using spaces.
x = x.split("a")          #it split the sentence by using of the letter a
print(x)

#title                   #it will capitalize the first letter in the all words insentence.
x = "Hello bhanuprasad"
x = x.title()
print(x)

#lowercase               # it will do the given sentence will formed as lowercase.
x= "Hello bhanuprasad"
x = x.lower()
print(x)

#islower                  #it will do the boolean if its letters are in lower or not.
x = "Hello bhanuprasad"
x = x.islower()
print(x)

#uppercase               #this will do the given letters formed as uppercase.
x = "Hello bhanuprasad"
x = x.upper()
print(x)

#isupper                #it is used for boolean of the wors are in upper or not it will describes.
x = "Hello bhanuprasad"
x = x.isupper()
print(x)

#swapcase                        #it will swapcase will do the capital letters are to form smallar and smaller will convert capitals.
x = "Hello bhAnupRasad"
x = x.swapcase()
print(x)

#replace function              #it will replace the words in the sentences.
x = "Hello bhanuprasad"
x= x.replace("Hello","welcome")
print(x)

#isdigit                     #it will do bolean of the digits in the given variable if it having the one alphabet it will give false.
x = "486t"
x = x.isdigit()
print(x)

#isalpha                       #isalpha will describesthe boolean of spaces if spaces are in a sentence or word then it will gives as false.
x = "Hello bhanuprasad"
x= x.isalpha()
print(x)

#strip                         #it will remove extra charectors from the keft side and right side of the sentence or word in the alphabets.
x = "!!!!!!!!!!!!!!!!!!!!!!!mmmmmmmmmVVVVVVVHello gggggggggggg bhanuprasadVVVVVmmmmmmmmmmm!!!!!!!!!!!!!"
x = x.strip("!mVg")        # in this the middle strips wont be deleted in the word.
print(x)

#lstrip                 #it will remove the left side of the word.
x = "!!!!!!!!!!Hello bhanuprasad!!!!!!!!!!!!!!"
x= x.lstrip("!")
print(x)

#rstrip                #it is used for removing the variables from right side of the word.
x = "!!!!!!!!!!!Hello bhanuprasad!!!!!!!!!!!"
x = x.rstrip("!")
print(x)

