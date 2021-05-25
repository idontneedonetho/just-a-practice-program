while True:

    with open("cough_drops.txt", "r") as file:
        print(file.read())
    follow = input("Would you like to add more?(Please say (Y)es or (N)o: ").lower()
    if follow == ("yes") or follow == ("y"):
        exec(open('add.py').read())
    elif follow == ("no") or follow == ("n"):
        raise SystemExit
    else:
        print("Please choose one of the two options.")
        continue
    continue