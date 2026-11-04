def calc_retail_price(whole,mark):
    mark_dec = mark/100
    whole = whole * (1+mark_dec)
    return whole

def main():
    wholesale = float(input("Please enter a wholesale cost:\n"))
    markup = float(input("Please enter a markup percentage:\n"))

    wholesale = calc_retail_price(wholesale, markup)
    print(f"The retail price is £{wholesale:.2f}.")

# This is needed for the tests. This is now the first bit of code Python will run.
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
    #main()  # calls the main function

    # uncomment the following lines to test calc_retail_price when you run the program.You will need to comment out main()
    print(calc_retail_price(3.00, 100)) # should print 6.0
    print(calc_retail_price(5.00, 50)) # should print 7.5