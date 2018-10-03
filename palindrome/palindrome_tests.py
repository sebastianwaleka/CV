from palindrome import palindrome

def test_palindrome_empty():
    assert palindrome('') == 'No text found!'


def test_palindrome_correct():
    assert palindrome('kajak') == 'It\'s palindrome.'
    assert palindrome('lol') == 'It\'s palindrome.'
    assert palindrome('zaraz') == 'It\'s palindrome.'


def test_palindrome_false():
    assert not palindrome('bardzo') == 'Palindrome'
    assert not palindrome('interesting') == 'Palindrome'
    assert not palindrome('zając') == 'Palindrome'


def test_palindrome_one_letter():
    assert not palindrome('x') == 'Not palindrome.'

