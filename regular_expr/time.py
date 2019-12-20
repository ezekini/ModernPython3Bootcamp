import re
# Returns first instance of phone number pattern:


def is_valid_time(input):
    #different options. Last one is more complete
    #phone_regex = re.compile(r'^\d{1,2}:\d{1,2}$')
    #phone_regex = re.compile(r'^\d\d?:\d\d$')
    #phone_regex = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):[0-5][0-9]$')

    match = phone_regex.search(input)
    if match:
        return True
    return False


is_valid_time('10:45')
is_valid_time('1:23')
is_valid_time('10.45')
is_valid_time('1999')
is_valid_time('145:23')
