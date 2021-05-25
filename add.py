#I use this to add the number typed to the number in cough_drops.txt, and I'm sure there is a way more streamline way to do this
while True:

    #I use this 'question' variable to get the number someone wants to add to the current amount
    question = input("How many cough drops? ")

    #This opens the file, reads the current amount, then adds the user input number, then closes the text file
    file =  open("cough_drops.txt", "r+")
    answer = file.readline()
    final = int(question) + int(answer)
    file.seek(0)
    file.truncate()
    file.write(str(final))
    file.close()

    #This tells the user the number they put, then asks if they'd like to add more, or not
    print("Added %s cough drop(s) to your total." % (question))
    follow = input("Would you like to view your current amount? (Y)es or (N)o: ").lower()
    if follow == ("yes") or follow == ("y"):
        exec(open('read.py').read())
    elif follow == ("no") or follow == ("n"):
        raise SystemExit
        
    else:
        print("Please choose one of the two options.")
        continue
    continue