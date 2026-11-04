def tuple_search(t, search_index):
    Letter_count = t.count(search_index)
    Letter_index = t.index(search_index)
    return (Letter_count,Letter_index)


if __name__ == "__main__":
    # main code
    spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
    print(tuple_search(spaghetti_soup, "g")) # should print (3, 2)