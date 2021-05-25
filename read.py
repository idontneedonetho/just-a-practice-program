#I use this to read the file and print the number that is in cough_drops.txt
while True:

    #This gets right to it by opening the file and reading it, then printing the total
    with open("cough_drops.txt", "r") as file:
        print(file.read())

    #I then use 'follow' to get a user input as to what they want to do next, allowing the user to either add more or not
    follow = input("Would you like to add more? (Y)es or (N)o: ").lower()
    if follow == ("yes") or follow == ("y"):
        exec(open('add.py').read())
    elif follow == ("no") or follow == ("n"):
        raise SystemExit
        
    else:
        print("Please choose one of the two options.")
        continue
    continue