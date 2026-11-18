import json

def load(filename):
  with open(filename,"r") as f:
    file_content = json.load(f)

    f.close()
    return file_content

if __name__ == "__main__":
  print(load("./unit_07/src/lessons/Lesson_05_items.json"))

