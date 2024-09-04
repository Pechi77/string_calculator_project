class StringCalculator:
    """ A simple string calculator that can add numbers
     separated by a delimiter.
    """
    def add(self, numbers: str) -> int:
        if not numbers.strip():
            return 0
        
        delimiter = ","

        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
            
        numbers = numbers.replace("\n", delimiter)

        numbers = numbers.replace("\n", ",")
        nums = map(int, numbers.split(delimiter))

        return sum(nums)
        