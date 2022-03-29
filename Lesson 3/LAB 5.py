def tar8():
    color_list = ["Red", "Green", "White", "Black"]
    return f'{color_list[0]}, {color_list[-1]}'


def tar10(num):
    return sum([num * (10 ** j) for i in range(1, 4) for j in range(i)])


class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


def tar14(date1, date2):
    return f'{abs(date1.day - date2.day)} days, {abs(date1.month - date2.month)} months and {abs(date1.year - date2.year)} years '


def tar18(num1, num2, num3):
    s = sum([num1, num2, num3])
    if num1 == num2 and num2 == num3:
        return [s, s, s]
    return s


def tar149(num):
    if num > 0:
        return sum([(i**2)for i in range(num)])
    return 0


def main():
    print(tar8())
    print(tar10(5))
    print(tar14(date(2, 7, 2014), date(11, 7, 2014)))
    print(tar18(3, 3, 3))
    #זה תרגילים ממש קלים, אני מדלג לאחרון
    print(tar149(3))


main()
