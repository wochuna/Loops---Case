day = input("Enter days of the week (Monday - Sunday): ").lower()

match day:
    case "monday":
        print("Uuufff!!!")
    case "tuesday":
        print("God!!")
    case "wednesday":
        print("Halfway There")
    case "thursday":
        print("Almost there")    
    case "friday":
        print("Yeey")
    case "saturday" | "sunday":
        print("Weekend vibes")
    case _:
        print("Invalid Day")          