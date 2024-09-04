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
        nums = list(map(int, numbers.split(delimiter)))
        negatives = [str(n) for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives[0]}")
        return sum(nums)
        