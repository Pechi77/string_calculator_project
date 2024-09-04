class StringCalculator:
    """ A simple string calculator that can add numbers
     separated by a delimiter.
    """
    def __init__(self):
        self._called_count = 0
    
    
    def get_called_count(self) -> int:
        """ Get the number of times the add method was called."""
        return self._called_count

    def add(self, numbers: str) -> int:
        """ Add numbers separated by a delimiter."""
        self._called_count += 1

        if not numbers.strip():
            return 0
        
        delimiter = ","

        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
            
        numbers = numbers.replace("\n", delimiter)

        numbers = numbers.replace("\n", ",")
        nums = list(map(int, numbers.split(delimiter)))
        negatives = [str(n) for n in nums if n < 0]
        if negatives:
            if len(negatives) > 1:
                raise ValueError(f"negatives not allowed: {', '.join(negatives)}")
            raise ValueError(f"negatives not allowed: {negatives[0]}")
        return sum(nums)
        