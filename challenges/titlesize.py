'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


def titleize(sentence):
    data = sentence.split()
    new_str = ''
    for word in data:
        new_str += word[0].title() + word[1:] + ' '
    new_str = new_str[:-1]
    return print(new_str)


titleize('this is awesome')  # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt')  # "ONLy CAPITALIZe FIRSt"
