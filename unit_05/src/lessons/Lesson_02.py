
def reverse(str_to_reverse):
    return(str_to_reverse[::-1])

def get_character(string_one, i):
    return(string_one[i-1])   

if __name__ == "__main__":
    print(reverse("This is a string")) # prints "gnirts a si sihT"
    print(reverse("Hello World")) # prints "dlroW olleH"
    print(get_character("This is a string", 3)) # prints "i"
    print(get_character("Hello World", 5)) # prints "o"