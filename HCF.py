class HCF:
    numbers = []
    factors_num1 = []
    factors_num2 = []
    HCF = 0

    def __init__(self, numbers, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        self.numbers = numbers

    def factorise(self):
        """
        appends the factors of num1 and num2 to their respective lists
        """
        i = 2
        while i <= self.num1:
            if self.num1 % i == 0:
                self.num1 /= i
                self.factors_num1.append(i)
                continue
            i += 1

        i = 2
        while i <= self.num2:
            if self.num2 % i == 0:
                self.num2 /= i
                self.factors_num2.append(i)
                continue
            i += 1

    @classmethod
    def getHCF(cls, numbers=None):
        # Pseudocode:
        # for (i:1 to m):
        #     if (i divides m & i divides n):
        #         HCF = i    -> keeps updating

        if numbers is None:
            numbers = cls.numbers
            m = numbers[0]
            j = 2147483647
            for i in numbers:
                if i < j:
                    j = i
                    m = i
        else:
            m = numbers[0]
            j = 2147483647
            for i in numbers:
                if i < j:
                    j = i
                    m = i

        for i in range(1, m + 1):
            for num in numbers:
                if num % i != 0:
                    break
            else:
                cls.HCF = i

        return cls.HCF


if __name__ == '__main__':
    print(HCF.getHCF([150, 200, 250, 75, 125, 50]))
