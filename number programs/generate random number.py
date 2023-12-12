import random
random = random.random()
print(random)

#uniform
import random
unif = random.uniform(10.4,13.4)
print(unif)

#randint
import random
num = random.randint(12,23)
print(num)

#bits
import random
b = random.getrandbits(12)
print(b)

#choice
import random
list = [1, 2, 3, 4, 5, 6]
print(list)
c = random.choice(list)
print(c)


#test cases
#1:its verify that ithe generated number is betwen 0 and 1
#2:a,b can give that different values and its generated the floating values in between them
#3:a is equal to b then the generated value is a
#4: its generated with in the range of values
#5:if k is equal to 0 then its get the result is 0 else we can give bits then it will gives numbers
#6: provinding list should be geytting the result as random and we provided empty list thats gives as error