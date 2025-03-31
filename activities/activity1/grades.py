def calc_grade(grade):
        if grade > 90:
            return "A"
        elif (90>grade>80):
            return "B"
        elif (80>grade>70):
            return "C"
        elif (70>grade>60):
            return "D"
        elif (grade<60):
            return "F"
        else:
            return "Not a valid grade!"

