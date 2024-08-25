sum = 0.0
while True:
    data=(input("Enter a number or just enter to quite: "))
    if data=="":
        break
    number=float(data)
    sum=sum+number
print ("The sum is: ", sum)
               