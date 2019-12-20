import csv


def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    contador = 0
    with open('users.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                contador += 1
            else:
                csv_writer.writerow(row)
    return print("Users updated: {}.".format(contador))


update_users("Grace", "Hopper", "Hello", "World")  # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett")  # Users updated: 2.
update_users("Not", "Here", "Still not", "Here")  # Users updated: 0.
