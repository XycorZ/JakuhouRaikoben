import sys
import collections

def load_file(filename):
  with open(filename,"r") as f:
    lines = f.read()
    return lines  
  
def count_letters(filename):
  words = load_file(filename)
  words_count = collections.Counter(words)

  words_count = dict(sorted(words_count.items(), key = lambda x: x[0]))

  print("The count of the letters for the file is:\n")
  for k,v in words_count.items():
    if k.isalpha() == False:
      del k
    else:
      print(f"{k}: {v}") 

    
if __name__ == "__main__":
  count_letters("./unit_07/src/exercises/Exercise_04_words.txt")