import doctest
def factorial(num):
    """
    calculate the factorial of positive number.

    Parameters:
        
        num(int): a positive number.

    Returns:
        int: The factorial of input num

    Raises:
        ValueError: num must be positive!

    Examples:
        >>> factorial(2)
        2
        >>> factorial(0)
        100
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: num must be positive!
    """
    if num < 0:
        raise ValueError("num must be positive!")
    if num == 0:
        return 1
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

def add(x, y):
    """
    sum of two numbers:

    Parameters:
        x(int): number1
        y(int): number2

    Returns:
        int: result
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(3, 5)
        7
    """
    return x+y


if __name__ == "__main__":
    print(factorial(7))
    doctest.run_docstring_examples(factorial, globals())
    #doctest.testmod()
