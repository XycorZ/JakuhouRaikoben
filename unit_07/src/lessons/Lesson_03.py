def number_of_lines(filename):
  with open(filename,"r") as f:
    lines = f.readlines()
    count = 0
    for x in lines:
      count+=1

  f.close()
  return count

def main():
  print(number_of_lines("./unit_07/src/lessons/Lesson_03_example.txt"))  # prints 9
  print(number_of_lines("./unit_07/src/lessons/Lesson_03_test.txt"))     # prints 25

if __name__ == "__main__":
  main()
