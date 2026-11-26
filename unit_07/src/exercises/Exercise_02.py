import json

def add_item(menu_dict, name, price):
  pos = str(menu_dict['next_id'])
  menu_dict['menu'].update({pos:{"Name":name,"Price":float(price)}})
  menu_dict['next_id']+=1

def load(filename):
  with open(filename,"r") as f:
    loaded_file = json.load(f)
    return loaded_file

def save(filename, menu_dict):
  with open(filename,"a") as f:
    f.write(json.dumps(menu_dict))

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
