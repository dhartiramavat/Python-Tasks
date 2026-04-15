num = int(input("Enter number: "))

match num:
    case n if n > 0:
        print("Positive number")
    case n if n < 0:
        print("Negative number")
    case _:
        print("Zero")


