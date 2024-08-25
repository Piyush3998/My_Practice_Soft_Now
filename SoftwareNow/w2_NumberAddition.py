'''
print("number addition program in range defined")

lower= int(input("Enter the lower bound num: "))
upper= int(input("Enter the higher bound num: "))
sum = 0
for count in range (lower,upper+1):
    sum = sum +count

print("SUM is: ", sum)
'''

print("Addition of even numbers program")

sum=0

for count in range (3,10,2):
    sum=sum+count

print("Sum is ",sum)