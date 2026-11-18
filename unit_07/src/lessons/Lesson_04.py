def write_nums(n):
  with open("./unit_07/src/lessons/Lesson_04_nums.txt","w") as f:
    for x in range(1,n+1):
      f.write(f"{str(x)}\n")

  f.close()

if __name__ == "__main__":
  write_nums(10) 
  # writes out the first 10 positive numbers to nums.txt