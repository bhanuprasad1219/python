n = (int(input("enter a decimal number:")))
binary = []
if(n==0)
    binary.append()

for n>0 in binary
    r=n%2
    binary.apprnd(r)
    n=n//2
# Get the decimal number from the user
n = int(input("Enter a decimal number: "))

# Initialize an empty list to store binary digits
binary = []

# Handle the case where n is 0 separately
if n == 0:
    binary.append(0)

# Convert decimal to binary
while n > 0:
    remainder = n % 2
    binary.append(remainder)
    n = n // 2

# Reverse the list to get the binary representation in the correct order
binary.reverse()

# Print the binary number
print("Binary number is:", end=" ")
for digit in binary:
    print(digit, end="")

print()  # Print a newline for better
