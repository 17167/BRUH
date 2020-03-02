backpack = ["food", "water", "money"]


while True:
    user = input("Welcome to the backpack from the bushes my brodda, pick a number\n 1. Add Item\n 2. Remove Item\n 3. Search yer backpack\n 4. View yer backpack\n 5. Exit\n")

    if user == "1":  #adding stuff
        while True:
            addstuff = input("Tell me what ya wanna add, type exit if you wanna do something else\n")
            if addstuff == "exit": #if the user wants to change option
                break
            backpack.append(addstuff)
            print("Item has been added\n")

    elif user == "2": #removing stuff
        while True:
            removestuff = input("Tell me what ya wanna remove, type exit if you wanna do somthing else\n") 
            if removeitem == "exit": #if the user wants to change option
                break
            if removestuff in backpack:
                backpack.remove(removestuff)
            else:
                print("Can't remove stuff you don't have lmao try again\n")     

    elif user == "3": #search fer stuff
        item = input("What ya looking for bucko\n")
        if item in backpack:
            print("Yes it's in there")
        else:
            print("You don't have it")

    elif user == "4": #look at the backpack
        if not bool(len(backpack)): #detects if there's anything in the backpack
            print("The backpack is empty, nothing but dust\n")
        for item in backpack:
            print(item)
        

    elif user == "5": #exit le program
        print("Buh Bye now")
        break        

    else: #when picking a foreign option
        print("That's not an option buddy, pick another\n")