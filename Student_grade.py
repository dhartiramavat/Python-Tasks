score = int(input("Enter the student's score: "))

if 0 <= score <= 100:
    match score:
        case s if s >= 90:
            print("Grade: A")
        case s if s >= 80:
            print("Grade: B")
        case s if s >= 70:
            print("Grade: C")
        case s if s >= 60:
            print("Grade: D")
        case _:
            print("Grade: F")
else:
    print("Error: Score must be between 0 and 100.")