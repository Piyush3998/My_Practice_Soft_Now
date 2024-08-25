print("Number guess program")

number =23
running= True

while running:
    guess=(int(input("Enter the number: ")))
    if guess == number:
        print("Congratulations! You guesed the number right.")
        running=False
    elif guess<number:
        print("You are a bit short for the number!")
    elif guess>number:
        print("You are a bit higher than the actual number! ")

print("Done.")