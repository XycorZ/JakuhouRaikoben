def print_list(list, multiple = 1):
    for x in range (0,len(list)):
        print (f"{list[x]*multiple}")
    

if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])