#elif
x = 10
y = 20
z = 30
if x > y:
    print("x is greater than y")
elif y > z:
    print("y is greater than z")
else:
    print("z is greater than x")

#nested if

x = "bhanu"
y = "clg"
z = 87
if y == "clg":        # the statement is true then it will move to next condition
    if x == "bhanu":  # this both statements are true then it will print the values
        print(z)