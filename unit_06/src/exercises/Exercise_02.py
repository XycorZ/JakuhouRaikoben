import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():
    ranges={
        10:0,
        20:0,
        30:0,
        40:0,
        50:0
    }
    rand_num_list = rand_num_list_gen()
    for x in rand_num_list:
        if 1<=x<=10:
            ranges[10]+=1
        if 11<=x<=20:
            ranges[20]+=1
        if 21<=x<=30:
            ranges[30]+=1
        if 31<=x<=40:
            ranges[40]+=1
        if 41<=x<=50:
            ranges[50]+=1
    
    print(f"I have generated 100 random numbers between 1 and 50.\nThe count in the following ranges is:")
    print(f"1..10: {ranges[10]}")
    print(f"11..20: {ranges[20]}")
    print(f"21..30: {ranges[30]}")
    print(f"31..40: {ranges[40]}")
    print(f"41..50: {ranges[50]}")

def advanced_main():
    #getting input (//TESTING NOTES: WORKS AS INTENDED) 
    num_to_gen = input("Please enter the number of integers to generate between 1 and 50:\n")
    ranges = input("Please enter the ranges in the following format 1..5,6..10,11..20\n")
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))
    
    #separating the bins that we got in first part. (//TESTING NOTES: WORKS AS INTENDED)  
    ranges_dict = {}
    splitting = ranges.split(",")
    for x in splitting:  
        ranges_dict.update({x:0})
    
    # #sorts and packs the bins. (//TESTING NOTES: WORKS AS INTENDED)  
    print("The count in the given ranges is:\n")
    for x in ranges_dict:
        sorter=x.split("..")
        sorter=list(map(int, sorter))

        lower_limit = sorter[0]
        upper_limit = sorter[1]

        for z in rand_num_list:
            if lower_limit<=z<=upper_limit:
                ranges_dict[x]+=1    

    #output the bins  (//TESTING NOTES: WORKS AS INTENDED)      
    for x,y in ranges_dict.items():
        print(f"{x}: {y}")

if __name__ == "__main__":
    #main()
    advanced_main()