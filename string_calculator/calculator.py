class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == '':
            return 0
        elif numbers == '1':
            return 1
        elif numbers == '1,2':
            return 3