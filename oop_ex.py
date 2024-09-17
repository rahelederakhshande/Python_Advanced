#import doctest
class Calculator:
    """
    A simple caclculator.

    Examples:
        >>> obj = Calculator()
        >>> obj.add(2, 3)
        5
    """
    def add(self, x, y):
        """
        sum of two numbers:

        Parameters:
            x(int): number1
            y(int): number2

        Returns:
            int: result
        
        Examples:
            >>> obj = Calculator()
            >>> obj.add(2, 3)
            5
            >>> obj.add(3, 5)
            8
        """
        return x+y
    
    def subtract(self, x, y):
        """
        subtract of two numbers:

        Parameters:
            x(int): number1
            y(int): number2

        Returns:
            int: result
        
        Examples:
            >>> obj = Calculator()
            >>> obj.subtract(2, 3)
            -1
            >>> obj.subtract(3, 5)
            -2
        """
        return x-y

# python3 -m doctest -v oop_ex.py    
"""if __name__ == "__main__":
    #doctest.testmod(verbose=True)
    doctest.run_docstring_examples(Calculator.add, globals())"""