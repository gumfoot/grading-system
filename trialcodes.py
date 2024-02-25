def assign_grades():
 grades = int(input("Insert Marks: "))
 if grades > 100:
    print ("Invalid input")
 elif grades >= 90:
    print("You got an A!")
 elif grades >= 80:
    print ("You got an A-")
 elif grades >= 70:
    print("You got a B+")
 elif grades >= 60:
    print ("You got a B")
 else:
    print("You failed beyond measure")
assign_grades()