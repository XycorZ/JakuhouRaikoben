def longest_word(string_list):
    if string_list == []:
        return None
    else:
        maxxing = []
        for x in string_list:
            for y in x:
                maxxing.append(y)
        return (max(maxxing, key=len))
  
def num_characters(string_list):
        total = 0
        for x in string_list:
            for y in x:
                total += len(y)
        return total
  
if __name__ == "__main__":
    test_string = [["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]
    test_string2 = [["Hello", "World"], ["Apple", "Pears"]]
    print(longest_word(test_string)) # should print revolution
    print(num_characters(test_string)) # should print 105
    print(longest_word(test_string2)) # should print hello
    print(num_characters(test_string2)) # should print 20
