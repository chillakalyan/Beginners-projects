print("\t \t \t \t *****************\t \t \t \t \t")
print("Welcome to the Guessing The Number")

import random
small_num=int(input("Enter your small number:"))
large_num=int(input("Enter your large number:"))
system_selected=random.randint(small_num,large_num)
count=0
while True: # we should use while loop but we use without any condition directly we written True
    count+=1
    user_selected=int(input("Enter your guess number:"))
    if user_selected<system_selected:
        print("Too small")
    elif user_selected>system_selected:
        print("Too big")    
    else:
        print("Congratulations! You've got it in", count, "tries!")    
        break #use break or exit()