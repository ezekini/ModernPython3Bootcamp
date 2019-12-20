'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(string_, n):
    if n < 3:
        return print('Truncation must be at least 3 characters.')
    if n > len(string_):
        return print(string_[:n - 3])
    return print(string_[:n - 3] + '...')


truncate("Super cool", 2)  # "Truncation must be at least 3 characters."
truncate("Super cool", 1)  # "Truncation must be at least 3 characters."
truncate("Super cool", 0)  # "Truncation must be at least 3 characters."
truncate("Hello World", 6)  # "Hel..."
truncate("Problem solving is the best!", 10)  # "Problem..."
truncate("Another test", 12)  # "Another t..."
truncate("Woah", 4)  # "W..."
truncate("Woah", 3)  # "..."
truncate("Yo", 100)  # "Yo"
truncate("Holy guacamole!", 152)  # "Holy guacamole!"
