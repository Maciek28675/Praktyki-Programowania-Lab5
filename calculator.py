class Calculator:
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
        return a - b
    
    @staticmethod
    def multiply ( a: int , b: int) -> int:
        return a * b
    
    @staticmethod
    def divide ( a: int , b: int) -> float :
        try:
            return a / b
        except ZeroDivisionError as e:
            print("Error: division by zero is forbidden!")
            return(float('NaN'))