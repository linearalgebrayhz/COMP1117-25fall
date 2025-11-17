def sum_digit(n:int)->int:
    """Summing up digits in a number

    Args:
        n (int): input number

    Returns:
        int: sum of the digits in the input number
    """
    if n < 10:
        return n
    else:
        return sum_digit(n//10) + n % 10   
    

# Mutual recursion example from last Tutorial
def sum_odd(n):
    if n < 10:
        return n*2
    else:
        return sum_even(n//10) + (n % 10) * 2
    
def sum_even(n):
    if n < 10:
        return n
    else:
        return sum_odd(n//10) + n % 10