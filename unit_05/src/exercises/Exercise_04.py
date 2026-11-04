def arithmetic_sum(a,d,n):
    result = (n*(2*a + (n-1)*d))/2
    return int(result)

if __name__ == "__main__":
    print(arithmetic_sum(1,1,100))   # prints the return value - 5050
    print(arithmetic_sum(3,2,15))    # prints the return value -  255
    print(arithmetic_sum(10,4,5))    # prints the return value -  90
    print(arithmetic_sum(-5, -2, 20))    # prints the return value -  -480