try:
    log_file = input("Enter log file: ")
    with open(log_file) as file:
        print("File opened successfully")
        print("Total Lines: ", len(file.readlines()))
except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong!")
