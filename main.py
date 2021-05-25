#This is a super simple program that I made in like, 5 days
while True:

    #Get's user input
    options = input("What would you like to to do? (Add, Amount or Clear) ").lower()
    if options == ("add"):
        exec(open('add.py').read())
    elif options == ("amount"):
        exec(open('read.py').read())

    #Opens file, goes to the front of the file, resets? the file, then puts '0' and closes
    #I think this can be way smaller and more streamline, I just can't figure out how
    elif options == ("clear"):
        zero = 0
        file = open("cough_drops.txt", "r+")
        file.seek(0)
        file.truncate()
        file.write(str(zero))
        file.close()
        print("Cleared.")
        
    else:
        print("Please choose one of the two options.")
        continue
    continue