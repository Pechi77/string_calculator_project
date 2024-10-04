import re
from functools import wraps

def preprocess_input(func):
    @wraps(func)
    def wrapper(self, numbers: str) -> int:
        self._called_count += 1

        if not numbers.strip():
            return 0

        delimiter = ","

        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter_part = parts[0][2:]
            numbers = parts[1]
            delimiter_regex = "|".join(map(re.escape, delimiter_part))
        
        else:
            delimiter_regex = re.escape(delimiter)
            numbers = numbers.replace("\n", delimiter)

        nums = list(map(int, re.split(delimiter_regex, numbers)))

        return func(self, nums)
    return wrapper

class StringCalculator:
    """ A simple string calculator that can add numbers
     separated by a delimiter.
    """
    def __init__(self):
        self._called_count = 0
    
    def get_called_count(self) -> int:
        """ Get the number of times the add method was called."""
        return self._called_count

    @preprocess_input
    def add(self, nums) -> int:
        
        if nums == 0:
            return 0
        
        nums = [num for num in nums if num <= 1000]

        negatives = [str(n) for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(negatives)}")

        return sum(nums)
