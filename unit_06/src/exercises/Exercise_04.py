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

        coins = {
            50: 0,
            20: 0,
            10: 0,
            5:  0,
            2:  0,
            1:  0
        }

        if (return_change//50) >= 1:
            coins[50] += return_change//50
            return_change-=50
        if (return_change//20) >= 1:
            coins[20] += return_change//20
            return_change-=20
        if (return_change//10) >= 1:
            coins[10] += return_change//10
            return_change-=10
        if (return_change//5) >= 1:
            coins[5] += return_change//5
            return_change-=5
        if (return_change//2) >= 1:
            coins[2] += return_change//2
            return_change-=2
        if (return_change//1) >= 1:
            coins[1] += return_change//1
            return_change-=1

        for x,y in coins.items():
            print(f"Number of {x}p coins is {y}")

if __name__ == "__main__":
    main()
