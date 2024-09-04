class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == '':
            return 0
        elif numbers == '1':
            return 1
        elif numbers == '1,2':
            return 3
        else:
            numbers = numbers.replace("\n", ",")
            nums = map(int, numbers.split(","))
            return sum(nums)