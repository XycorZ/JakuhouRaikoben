# Place your answer to Exercise_06 in this file
# Do not rename or remove this file

# Do not touch this line
input_list = list(input("Please enter a list of strings separated by a comma.\ne.g. one,two,three,four,five\n\n").split(','))

min_index = 0
max_index = 0
total = 0

i = 0

while i < len(input_list):
  total += len(input_list[i])
  if len(input_list[i]) > len(input_list[max_index]):
    max_index = i

  if len(input_list[i]) < len(input_list[min_index]):
    min_index = i
  i+=1

print(f"The minimum length of a string is {len(input_list[min_index])}")
print(f"The maximum length of a string is {len(input_list[max_index])}")
print(f"The average length of the strings in the list is {total/len(input_list):.2f}")