def load_grid(filename):
  with open(filename, "r") as f:
    lines = f.readlines()
    
    combined = []
    pure = []
    for x in lines:
      point = x.strip().split(" ")
      combined.append(list(point))

    for y in combined:
      for z in y:
        pure.append(list(map(int,z))) #writes the files into a 2d array

    return pure

def max_num_in_rows(grid, num_digits):
  maximum = max(grid)
  number = ''.join(map(str,maximum[0:num_digits])) 
  # finds the row with the largest array value, then prints the first to n-digit of 
  # said array as a single number
  return int(number)

def max_num_adv(grid, num_digits):
  #left to right
  Left2Right = max(grid)
  number_L2R = ''.join(map(str,Left2Right[0:num_digits])) #same as max_num_in_rows
  number_L2R = int(number_L2R)

  #diagonally top-left to bottom-right
  coloums = len(grid[0])
  rows = len(grid)
  total_diagonals = (coloums + rows) - 1
  diagonals_TL2BR = []
  
  TLeft2BRight = max(grid)
  number_TL2BR = ''.join(map(str,TLeft2BRight[0:num_digits])) #same in max_num_in_rows
  number_TL2BR = int(number_TL2BR)

  #diagonally bottom-left to top-right
  

  BLeft2TRight = max(grid)
  number_BL2TR = ''.join(map(str,BLeft2TRight[0:num_digits])) #same in max_num_in_rows
  number_BL2TR = int(number_BL2TR)


    #top to bottom
  for x in range(len(grid)-1): # function to transpose the matrix
    for y in range(x+1,len(grid)):
      grid[x][y], grid[y][x] = grid[y][x], grid [x][y]

  Top2Bottom = max(grid)
  number_T2B = ''.join(map(str,Top2Bottom[0:num_digits])) #same in max_num_in_rows
  number_T2B = int(number_T2B)


  #array of the largest n-digit number from the 4 ways of transposing the matrix
  # then returning the largest one  
  check4Max = [number_TL2BR,number_BL2TR]

  return max(check4Max)

def print_grid(grid):
  for line in grid:
    for x in line:
      print(f"{x}", end=" ")
    print("\n")

if __name__ == "__main__":
  filename = "./unit_07/src/exercises/Exercise_05_grid_5_by_5.txt"
  grid = load_grid(filename)
  print_grid(grid)  # print the grid
  print(max_num_in_rows(grid, 3))  # prints 912
  print(max_num_adv(grid, 3))  # prints 971
