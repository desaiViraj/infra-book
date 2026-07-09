file = input("Enter file name: ")
with open(file) as doc:
    print("Length of Doc :", len(doc.readlines()))
