import random as ran

def coin_tosses(n):
    tosses = []
    headsTails = [0,1]
    flattenedTosses = []
    for x in range(0,n):
        toss_flip = ran.sample(headsTails, k = 1)
        tosses.append(toss_flip)

    flattenedTosses = []
    for x in tosses:
        for y in x:
            flattenedTosses.append(y)
    
    return flattenedTosses



def count(tosses):
    heads = 0
    tails = 0
    for x in tosses:
        if x == 0:
            tails+=1 
        elif x == 1:
            heads+=1
    return heads,tails



def percentage(count_of_tosses):
    total_count = count_of_tosses[0]+count_of_tosses[1]
    percentage_of_heads = round(((count_of_tosses[0]/total_count)*100),2)
    percentage_of_tails = round(((count_of_tosses[1]/total_count)*100),2)
    return percentage_of_heads,percentage_of_tails


def main():
    x = input("How many coin tosses would you like to simulate?\n")
    toss_count = coin_tosses(int(x))

    total_count = count(toss_count)
    print(f"No. of Heads: {total_count[0]}")
    print(f"No. of Tails: {total_count[1]}")
    
    total_percentage = percentage(total_count)
    print(f"%   of Heads: {total_percentage[0]}")
    print(f"%   of Tails: {total_percentage[1]}")
    


if __name__ == "__main__":
    main()