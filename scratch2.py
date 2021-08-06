from csv import writer, reader, DictReader

# with open("cats.csv", "a") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Bo", 31])

def add_user(first_name, last_name):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow(["First Name", "Last Name"])
        csv_writer.writerow([first_name, last_name])

def print_users():
    with open("users.csv") as file:
        data = reader(file)
        ld = list(data)
        for i in ld[1:]:
            print(i[0]+" "+i[1])


def find_user(first_name, last_name):
    with open("users.csv") as file:
        data = reader(file)
        ld = list(data)
        for i in ld:
            if i[0] == first_name and i[1] == last_name:
                return ld.index(i)
        return first_name + " " + last_name + " not found."

# print(find_user('Colt', 'Steele'))

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv", "r") as csvfile:
        csv_reader = reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: " + str(count)
# update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
# update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
# update_users("Not", "Here", "Still not", "Here") # Users updated: 0.

def delete_users(old_first, old_last):
    with open("users.csv", "r") as csvfile:
        csv_reader = reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: " + str(count) + "."


delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.