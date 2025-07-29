user = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

if user == "42":
    print("yes")
elif user == "forty two":
    print("yes")
elif user == "forty-two":
    print("yes")
else:
    print("no")    