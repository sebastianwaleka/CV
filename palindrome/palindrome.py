'''
Program will check if given string is palindrome or not.
If it is, it will return str "It's palindrome" else "Not palindrome".
'''


def palindrome(text):
    if len(text) > 1:
        if text == text[::-1]:
            return 'It\'s palindrome.'
        else:
            return 'Not palindrome.'
    elif text == '':
        return 'No text found!'
    else:
        return 'Text too short.'

