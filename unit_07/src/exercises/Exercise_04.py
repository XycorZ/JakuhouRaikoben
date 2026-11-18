import sys

def load_file(filename):
  with open(filename,"r") as f:
    lines = f.readlines()
    pure_letters = [] 
    accept = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for x in lines:
      stripped = x.strip()
      split = stripped.split()
      for y in split:
        for z in y:
          if z in accept:
            pure_letters.append(z)
          elif z not in accept:
            y.strip(z)
    
    return pure_letters

    # really memory inefficient. takes 386 bytes to store the array of letters.
    # try optimize this for better. Mo 3:34am 18//11//2026 

    


    

def count_letters(filename):
  words = load_file(filename)
  pass

    
if __name__ == "__main__":
  count_letters("./unit_07/src/exercises/Exercise_04_words.txt")
