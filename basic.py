# Take three numbers from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find the largest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest= b
else:
    smallest = c

# Display the result
print("The smallest number is:", smallest)