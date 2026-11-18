def count_words(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
        splitted = []
        t_count = 0

        for x in lines:
            stripped = x.strip()
            splitted = stripped.split()
            for y in splitted:
                t_count+=1

        f.close()
        return t_count



        
def main():
    print(count_words("./unit_07/src/exercises/Exercise_01_example.txt"))  # should print 15

if __name__ == "__main__":
    main()
