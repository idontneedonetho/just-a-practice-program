while True:

    question = input("How many cough drops? ")
    file =  open("cough_drops.txt", "r+")
    answer = file.readline()
    final = int(question) + int(answer)
    file.seek(0)
    file.truncate()
    file.write(str(final))
    file.close()
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