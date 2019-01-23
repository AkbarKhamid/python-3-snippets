import csv


def find_user(name, last_name):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            if row[0] == name and row[1] == last_name:
                return index
        return "{} {} not found".format(name, last_name)


print(find_user('Colt', 'Steele'))
