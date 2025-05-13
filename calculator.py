"""
"""

class Calculator:
    """
    """
    def __init__(self):
        pass

    @staticmethod
    def add(a: int, b: int) -> int:
        """
            Caluclates sum of 2 given numbers.

            Args:
                a (int): First number.
                b (int): Second number.

            Returns:
                sum of a and b.
        """

        return a+ b

    @staticmethod
    def subtract ( a: int , b: int) -> int:
        """
            Caluclates difference of 2 given numbers.

            Args:
                a (int): First number.
                b (int): Second number.

            Returns:
                difference of a and b.
        """
        return a - b

    @staticmethod
    def multiply ( a: int , b: int) -> int:
        """
            Caluclates product of 2 given numbers.

            Args:
                a (int): First number.
                b (int): Second number.

            Returns:
                product of a and b.
        """
        return a * b

    @staticmethod
    def divide ( a: int , b: int) -> float :
        """
            Caluclates quotient of 2 given numbers.

            Args:
                a (int): First number.
                b (int): Second number.

            Returns:
                quotient of a and b.
        """
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: division by zero is forbidden!")
            return float('NaN')
