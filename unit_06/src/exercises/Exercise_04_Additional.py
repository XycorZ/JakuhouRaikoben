# ## Additional
# **The following is not tested, but is a good exercise for you to attempt. 
# I suggest you do it in a new Python file so as to not affect your existing code.**
# Try using a list to hold the values of the coins, so that you can write a general purpose 
# change calculator that can be used for any coinage simply by changing the contents of the 
# list (you might want to use a variable of type char to hold the coinage 
# (‘p’ for UK, ‘c’ for US, etc)).

# For example, once you have it working with UK coins (50, 20, 10, 5, 2, 1), 
# try changing the contents of the list so that it contains the US coin values 
# (25, 10, 5 and 1). Changing the contents of the list and the 
# contents of the char variable that contains the name of the currency in 
# use should be the only change you need to make to your program.



def main():
    amount = int(input("Please enter the amount inserted (1 to 100):\n"))
    if amount > 100 or amount <0:
        print('Invalid amount')
        return 0

    cost = int(input("Please enter the cost of the item:\n"))
    if amount < cost :
        print("Item costs more than amount inserted")
        return 0


    else:
        return_change = amount - cost
        currency_choice = input ("Enter which currency you are in: GBP/USD/CAD: ")

        coins_GBP = {
            50: 0,
            20: 0,
            10: 0,
            5:  0,
            2:  0,
            1:  0
        }

        coins_USD = {
            25:0,
            10:0,
            5:0,
            1:0
        }

        coins_CAD= {
            50:0,
            25:0,
            10:0,
            5:0,
            1:0
        }


        if currency_choice.upper() != "USD":
            if (return_change//50) >= 1: #gbp and cad have 50p
                coins_GBP[50] += return_change//50
                coins_CAD[50] += return_change//50
                return_change-=50

        if currency_choice.upper() == "GBP":
            if(return_change//20) >= 1: #only gbp has 20p
                coins_GBP[20] += return_change//20
                return_change-=20

        if currency_choice.upper() != "GBP":
            if (return_change//25) >= 1: #usd and cad have 25p
                coins_CAD[25] += return_change//25
                coins_USD[25] += return_change//25
                return_change-=25

        if (return_change//10) >= 1:
            coins_GBP[10] += return_change//10
            coins_CAD[10] += return_change//10
            coins_USD[10] += return_change//10
            return_change-=10

        if (return_change//5) >= 1:
            coins_GBP[5] += return_change//5
            coins_CAD[5] += return_change//5
            coins_USD[5] += return_change//5
            return_change-=5

        if currency_choice.upper() == "GBP":
            if (return_change//2) >= 1:
                coins_GBP[2] += return_change//2
                return_change-=2

        if (return_change//1) >= 1:
            coins_GBP[1] += return_change//1
            coins_CAD[1] += return_change//1
            coins_USD[1] += return_change//1
            return_change-=1

        if currency_choice.upper() == "GBP":
            for x,y in coins_GBP.items():
                print(f"Number of {x}p coins is {y}")

        if currency_choice.upper() == "CAD":
            for x,y in coins_CAD.items():
                print(f"Number of {x}c coins is {y}")

        if currency_choice.upper() == "USD":
            for x,y in coins_USD.items():
                print(f"Number of {x}c coins is {y}")

if __name__ == "__main__":
    main()
