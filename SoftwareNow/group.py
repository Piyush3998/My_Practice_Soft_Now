# Ask the user for three numbers
a = float(input("User input 1: "))
b = float(input("User input 2: "))
c = float(input("User input 3: "))

# Check if the three numbers can form a triangle using the triangle inequality theorem
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Yes, these three lengths can form a triangle.")
else:
    print("NO, these three lengths CANNOT form a triangle.")

# Ask the user for the size of the square
size = int(input("Enter the size of the square: "))
# Loop through each row to create the square
for i in range(size):
    if i == 0 or i == size - 1:
        # If it's the first or last row, print a full row of '*'
        # The space after each '*' makes the output clearer
        print('* ' * size)
    else:
        # For the middle rows, print a '*' at the beginning
        # Then print spaces to leave the inside empty
        # Finally, print a '*' at the end
        # Note: '  ' * (size - 2) adds spaces between the border '*' characters
        print('*' + '  ' * (size - 2) + ' *')
