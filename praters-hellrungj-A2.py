import math




def log_base_two(n):
    """ Takes in a number(n) and returns the logarithmic value of that number that has a base of 2."""

    return math.log(2, n)
    


def n_log_base_two(n):
    """ Time n times log base two and returns the value."""

    return n*math.log(2, n)


def n_to_two_power(n):
    """Returns the value of n squared"""
    return n*n
     
     
def two_to_n_power(n):
    """ Returns the value of 2 to the n squared. 
        Inside the for loop it mutilps the vaule by itself. 
        Then returns that value."""
    
    value = 2
    for i in range(n-1):
        value = value * value 
    return value
    

def factorial_n(n):
    """Takes in n and returns the value of n factorial """

    return math.factorial(n)
    
def main():
    n = 10
    print(log_base_two(n))
    print(n_log_base_two(n))
    print(two_to_n_power(n))
    print(n_to_two_power(n))
    print(factorial_n(n))
    n = 40
    print(log_base_two(n))
    print(n_log_base_two(n))
    print(two_to_n_power(n))
    print(n_to_two_power(n))
    print(factorial_n(n))

main()

