from itertools import cycle

class Book:
    def __init__(self, title, isbn):
        if not Book.__is_valid_title(title):
            raise RuntimeError("Invalid title")
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError("Invalid isbn")
        self.__title = title
        self.__isbn = isbn
    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    @staticmethod
    def __is_valid_title(title):
       return len(title) > 0
    
    @staticmethod
    def __is_valid_isbn(isbn):
        numbers = [int(number) for number in isbn if "0" <= number <= "9"]
        if len(numbers) != 13:
            return False
        weighted_sum = sum(digit * weight for digit, weight in zip(numbers, cycle([1, 3])))
        return weighted_sum%10 == 0