with open("connectedwallets2.txt") as f:
    a = (f.read().replace(",","."))
with open("connectedwallets2.txt", "w") as file:
        file.write(a)

    # a = (f.read().replace("DOUBLE","float"))
