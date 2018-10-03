'''
Program will generate personal ID with given birth date in format DD-MM-YYYY and sex.
Personal ID is valid when (1×a + 3×b + 7×c + 9×d + 1×e + 3×f + 7×g + 9×h + 1×i + 3×j + 1×k) is divisible by 10.
> For people born in 1900-1999 – month is writen as defualt 01-12
> For people born in different years following numbers must be added to month:
>> 1800–1899 – 80
>> 2000–2099 – 20
>> 2100–2199 – 40
>> 2200–2299 – 60.
'''

from random import randint, randrange


class Pesel:
    pesel_container = []

    def __init__(self, birth_date, sex):
        self.birth_date = birth_date.split('-')
        self.sex = sex
        self.year = self.birth_date[2]
        self.day = self.birth_date[0]
        self.month = self.birth_date[1]
        if len(self.birth_date[0]) == 4:
            self.year = self.birth_date[0]
            self.day = self.birth_date[2]
            self.month = self.birth_date[1]
        if len(self.year) != 4:
            raise ValueError('Wrong data format. Correct data format is DD-MM-YYYY or YYYY-MM-DD.')
        elif int(self.month) < 0 or int(self.month) > 12:
            raise ValueError('Wrong data format. There is 12 months.')
        elif int(self.day) < 0 or int(self.month) > 31:
            raise ValueError('Wrong data format. Correct data format is DD-MM-YYYY or YYYY-MM-DD.')
        self._num1 = int(self.year[-2])
        self._num2 = int(self.year[-1])
        # Year validation - adding numbers to month
        if 1900 <= int(self.year) <= 1999:
            self._num3 = int(self.month[0])
        elif 1800 <= int(self.year) <= 1899:
            self._num3 = int(self.month[0]) + 8
        elif 2000 <= int(self.year) <= 2099:
            self._num3 = int(self.month[0]) + 2
        elif 2100 <= int(self.year) <= 2199:
            self._num3 = int(self.month[0]) + 4
        elif 2200 <= int(self.year) <= 2299:
            self._num3 = int(self.month[0]) + 4
        self._num4 = int(self.month[1])
        self._num5 = int(self.day[0])
        self._num6 = int(self.day[1])
        if self.sex == 'm':
            self._num10 = int(randrange(1, 9, 2))
        elif self.sex == 'w' or self.sex == 'k':
            self._num10 = int(randrange(0, 9, 2))

    def generate(self):
        while True:
            self._num7 = randint(0, 9)
            self._num8 = randint(0, 9)
            self._num9 = randint(0, 9)
            self._num11 = randint(0, 9)
            _check = self._num1 * 1 + self._num2 * 3 + self._num3 * 7 + self._num4 * 9 + self._num5 * 1 + self._num6 * 3 + self._num7 * 7 + self._num8 * 9 + self._num9 * 1 + self._num10 * 3 + self._num11 * 1
            if _check % 10 == 0:
                break
        pesel = str(self._num1) + str(self._num2) + str(self._num3) + str(self._num4) + str(self._num5) + str(
            self._num6) + str(self._num7) + str(self._num8) + str(self._num9) + str(self._num10) + str(self._num11)
        if pesel not in Pesel.pesel_container:
            Pesel.pesel_container.append(pesel)
            return pesel
