with open("output.txt", "w") as file:
    for i in range(1, 10):
        file.write("a" * i+ "\n")