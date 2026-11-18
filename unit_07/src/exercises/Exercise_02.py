import json


def add_item(menu_dict, name, price):
  menu_dict.update({name:str(price)})


def load(filename):
  with open(filename,"r") as f:
    file_content = json.load(f)
    
    f.close()
    return file_content
    

def save(filename, menu_dict):
  with open(filename,"w") as f:
    for k,v in menu_dict.items():
      f.write(f"{k}:{v}\n")

    f.close()

def list_options():
  print("Option 1: List Menu")
  print("Option 2: Add Menu Item")
  print("Option 3: Quit")


def print_menu(menu_dict):
  print("\nMENU")
  print("----\n")
  for key, value in menu_dict["menu"].items():
    print(f"Item {key}\n")
    print(f"Name: {value['Name']}")
    print(f"Price: {value['Price']}\n")


def main():
  filename = "./unit_07/src/exercises/Exercise_02_menu.json"
  menu = load(filename)
  list_options()
  option = input("\nPlease select an option:\n")
  while option != "3":
    if option == "1":
      print_menu(menu)
    elif option == "2":
      name = input("\nPlease enter a name:\n")
      price = input("\nPlease enter a price:\n")
      add_item(menu, name, price)
      save(filename, menu)
    option = input("\nPlease select an option:\n")


if __name__ == "__main__":
  main()
