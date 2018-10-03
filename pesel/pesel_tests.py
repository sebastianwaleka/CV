from pesel import *

def test_pesel_class_initialize():
    pesel = Pesel('12-12-1988', 'm')
    assert pesel.year == '1988'
    assert pesel.month == '12'
    assert pesel.day == '12'
    assert pesel.sex == 'm'
    pesel = Pesel('1988-12-12', 'm')
    assert pesel.year == '1988'
    assert pesel.month == '12'
    assert pesel.day == '12'
    assert pesel.sex == 'm'

def test_pesel_generate():
    pesel = Pesel('12-12-1988', 'm')
    pesel.generate()
    assert (pesel._num1 * 1 + pesel._num2 * 3 + pesel._num3 * 7 + pesel._num4 * 9 + pesel._num5 * 1 + pesel._num6 * 3 + pesel._num7 * 7 + pesel._num8 * 9 + pesel._num9 * 1 + pesel._num10 * 3 + pesel._num11 * 1) % 10 == 0
    pesel = Pesel('15-01-1984', 'w')
    pesel.generate()
    assert (pesel._num1 * 1 + pesel._num2 * 3 + pesel._num3 * 7 + pesel._num4 * 9 + pesel._num5 * 1 + pesel._num6 * 3 + pesel._num7 * 7 + pesel._num8 * 9 + pesel._num9 * 1 + pesel._num10 * 3 + pesel._num11 * 1) % 10 == 0
    pesel = Pesel('15-01-1884', 'w')
    pesel.generate()
    assert (pesel._num1 * 1 + pesel._num2 * 3 + pesel._num3 * 7 + pesel._num4 * 9 + pesel._num5 * 1 + pesel._num6 * 3 + pesel._num7 * 7 + pesel._num8 * 9 + pesel._num9 * 1 + pesel._num10 * 3 + pesel._num11 * 1) % 10 == 0
