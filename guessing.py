import random 

smaller= int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

num = random.randint(smaller, larger)
count = 0
while  True:
    count+=1
    userNumber = int(input ("Input your guess:"))
    if userNumber < num:
        print("Too small!!")
    elif userNumber> num:
        print("Too large!!!")
    else:
        print("You've got it in ",count,"tries")
        break    
            