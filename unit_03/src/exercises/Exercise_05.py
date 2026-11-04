# Place your answer to Exercise_05 in this file
# Do not rename or remove this file

# This program converts a numeric grade to an alpha grade

input_bool = False

while not input_bool: 
    input_grade = int(input("Please enter the grade you wish to convert (0-100).\n"))
    if (input_grade < 0) or (input_grade > 100):
        print("ERROR: input not between 0 and 100\n")

    else:
        output_grade = ""
        if input_grade <= 34:
            output_grade = "F"
        elif input_grade <= 39:
            output_grade = "MF"
        elif input_grade <= 49:
            output_grade = "D"
        elif input_grade <= 59:
            output_grade = "C"
        elif input_grade <= 69:
            output_grade = "B"
        elif input_grade <= 79:
            output_grade = "A-"
        elif input_grade <= 89:
            output_grade = "A"
        else:
            output_grade = "A+"

        print(f"{input_grade} = {output_grade}.")
        input_bool = True