while True:

    options = input("What would you like to to do? (Add, Amount or Clear) ").lower()
    if options == ("add"):
        exec(open('add.py').read())
    elif options == ("amount"):
        exec(open('read.py').read())
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