import copy

def change_list(my_list):
    my_list1 = copy.deepcopy(my_list)
    my_list1[1] = 'Banana'
    my_list1.sort()
    return my_list1

if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]