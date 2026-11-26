import copy

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
  check4Max = []
  rows = len(grid)
  coloumns = len(grid[0])
  total_diagonals = rows + coloumns - 1 

  #left to right
  Left2Right = max_num_in_rows(grid,num_digits)
  check4Max.append(Left2Right)

  #diagonally top-left to bottom-right
  grid1 = copy.deepcopy(grid)
  diagonals_TL2BR = []
   
  for x in range(total_diagonals):
    if x < rows:
      z = 0
    else:
      z = x - rows + 1

    temp_diagonal1 = []
    for y in range(z, x - z + 1):
      temp_diagonal1.append(grid1[x - y][y])
    diagonals_TL2BR.append(temp_diagonal1)
 
  TLeft2BRight = max_num_in_rows(diagonals_TL2BR,num_digits)
  check4Max.append(int(TLeft2BRight))

  #diagonally bottom-left to top-right
  grid2 = copy.deepcopy(grid)
  diagonals_BL2TR = []
  
  #rotating the matrix 180 degrees
  for y in range(0,rows):
    start_of_row=0
    end_of_row=len(grid2)-1

    while(start_of_row<end_of_row):
      grid2[y][start_of_row], grid2[y][end_of_row] = grid2[y][end_of_row], grid2[y][start_of_row]
      start_of_row+=1
      end_of_row-=1

  for x in range(total_diagonals):
    if x < rows:
      z = 0
    else:
      z = x - rows + 1

    temp_diagonal2 = []
    for y in range(z, x - z + 1):
      temp_diagonal2.append(grid2[y][x - y])
    diagonals_BL2TR.append(temp_diagonal2)
 
  BLeft2TRight = max_num_in_rows(diagonals_BL2TR,num_digits)
  check4Max.append(int(BLeft2TRight))

  #top to bottom
  for x in range(rows-1): # function to transpose the matrix
    for y in range(x+1,rows):
      grid[x][y], grid[y][x] = grid[y][x], grid[x][y]

  Top2Bottom = max_num_in_rows(grid,num_digits)
  check4Max.append(Top2Bottom)

  #kargest n-digit number from the 4 ways of transposing the matrix
  # then returning the largest one  
  
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
