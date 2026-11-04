# Place your answer to Lesson_03 in this file
# Do not rename or remove this file

string_list = input("Please enter a list of numbers separated by a comma.\ne.g. Citreon,Ford,Audi,Mercedes\n").split(',')
for x in string_list:
    print(f"The length of the string {x} is {len(x)}.")