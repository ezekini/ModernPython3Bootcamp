'''
print_users() # None
# prints to the console:
# Colt Steele
'''
from csv import DictReader


def print_users():

    with open('users.csv') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            print(row['First Name'] + ' ' + row['Last Name'])


print_users()
