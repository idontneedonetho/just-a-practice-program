while True:

    options = input("What would you like to to do?(Please choose Add or Amount) ").lower()
    if options == ("add"):
        exec(open('add.py').read())
    elif options == ("amount"):
        exec(open('read.py').read())
    elif options == ("clear total"):
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