def add_and_subtract(num1, num2, num3):
    def sum_numbers():
        sum_nums = num1 + num2
        return sum_nums

    def subtract():
        result = sum_numbers() - num3
        return result

    return subtract()


num1, num2, num3 = int(input()), int(input()), int(input())

print(add_and_subtract(num1, num2, num3))
