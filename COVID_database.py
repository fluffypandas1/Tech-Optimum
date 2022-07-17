
class Database:

    def __init__(self, file):
        self.file = file

    def add(self, key, value):
        f = open(self.file, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()

    def select(self, key):
        f = open(self.file, 'r')
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                return v[:-1]
        f.close()
        return 0

    def delete(self, key):
        count = 0
        f = open(self.file, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
            else:
                count = 1
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.file)
        return count

    def update(self, key, value):
        count = 0
        f = open(self.file, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                result.write(key + '\t' + value + '\n')
                count = 1
            else:
                result.write(row)
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.file)
        return count



print("\nHello and welcome to HomeMed!\nFirst let's answer some questions to see how likely it is that you have COVID-19.")
counter = 0

# big symptoms, short breath, cough, fever/chills, fatigue, taste, sore throat, muscle/body aches
# source for symptoms: https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html


print("\nHave you been experiencing any fevers or chills? Enter \"y\" for yes and \"n\" for no.")
fever_chills_response = input().strip()
while fever_chills_response != "y" and fever_chills_response != "n":
    print("Please enter \"y\" or \"n\".")
    fever_chills_response = input().strip()
if fever_chills_response == "y":
    counter += 1

print("Have you been experiencing a cough? Enter \"y\" for yes and \"n\" for no.")
cough_response = input().strip()
while cough_response != "y" and cough_response != "n":
    print("Please enter \"y\" or \"n\".")
    cough_response = input().strip()
if cough_response == "y":
    counter += 1

print("Have you been experiencing any shortness of breath? Enter \"y\" for yes and \"n\" for no.")
short_breath_response = input().strip()
while short_breath_response != "y" and short_breath_response != "n":
    print("Please enter \"y\" or \"n\".")
    short_breath_response = input().strip()
if short_breath_response == "y":
    counter += 1

print("Have you been experiencing any fatigue? Enter \"y\" for yes and \"n\" for no.")
fatigue_response = input().strip()
while fatigue_response != "y" and fatigue_response != "n":
    print("Please enter \"y\" or \"n\".")
    fatigue_response = input().strip()
if fatigue_response == "y":
    counter += 1

print("Have you been experiencing any sudden loss of taste? Enter \"y\" for yes and \"n\" for no.")
taste_response = input().strip()
while taste_response != "y" and taste_response != "n":
    print("Please enter \"y\" or \"n\".")
    taste_response = input().strip()
if taste_response == "y":
    counter += 1

print("Have you been experiencing a sore throat? Enter \"y\" for yes and \"n\" for no.")
sore_throat_response = input().strip()
while sore_throat_response != "y" and sore_throat_response != "n":
    print("Please enter \"y\" or \"n\".")
    sore_throat_response = input().strip()
if sore_throat_response == "y":
    counter += 1

print("Have you been experiencing muscle or body aches? Enter \"y\" for yes and \"n\" for no.")
aches_response = input().strip()
while aches_response != "y" and aches_response != "n":
    print("Please enter \"y\" or \"n\".")
    aches_response = input().strip()
if aches_response == "y":
    counter += 1

print("The number of critical symptoms you are experiencing is : ", counter)

print("Based on the results of the questions...")

if counter >= 6:
    print("you most likely have COVID-19. Please answer the following prompts to store your contact information.")
    print("While entering your contact information, please be precise and remember what you enter. ")
    print("Failure to remember your information could result in your information being stuck in the database forever with no way to delete or update it, or you may simply be unable to view it via retrieval.")
    print("Please enter your first and last name.")
    name = input().strip()
    print('Please enter your phone number.')
    phone_number = input().strip()
    db = Database('db.txt')
    db.add(name, phone_number)
    print("Your information has been stored!")

if 2 < counter < 6:
    print("you may have COVID-19. To be safe, enter your contact information for consultation.")
    print("While entering your contact information, please be precise and remember what you enter. ")
    print("Failure to remember your information could result in your information being stuck in the database forever with no way to delete or update it, or you may simply be unable to view it via retrieval.")
    print("Please enter your full name.")
    name = input().strip()
    print('Please enter your phone number.')
    phone_number = input().strip()
    db = Database('db.txt')
    db.add(name, phone_number)
    print("Your information has been stored!")

if counter <= 2:
    print("You probably don't have COVID-19. Hope you recover soon!")
    quit()

while True:
    print("\nIf you want to remove, update, or access your information for viewing purposes, follow the instructions below.")
    print("To remove your information, please type \"r\". Please keep in mind that once you delete your information from the database,"
          " you will not be able to update or retrieve it. Thank you for understanding!")
    print("To update your phone number, please type \"u\".")
    print("To access your information, please type \"a\".")
    print("Or, if you are done using HomeMed, please enter \"q\" to exit the program.")

    choice = input().strip()
    while choice != "r" and choice != "u" and choice != "a" and choice != "q":
        print("Please enter one of the valid characters, listed above.")
        choice = input().strip()

    if choice == "r":
        print('Enter the name you would like to remove. *Case sensitive')
        remove = input().strip()
        db1 = Database('db.txt')
        value = db1.delete(remove)

        # User input validation
        while value == 0:
            print("The name you entered cannot be found, please try again. If you don't remember the name you entered, "
                  "please quit the program by entering \"quit\".")
            remove = input().strip()
            if remove == "quit":
                print("Thank you for using HomeMed!")
                quit()
            value = db1.delete(remove)

        print("Your information has been deleted!")


    if choice == "u":
        print("Enter the name associated with the number you would like to update. *Case sensitive")
        name1 = input().strip()
        print("Enter the new number.")
        number1 = input().strip()
        db1 = Database('db.txt')
        value = db1.update(name1, number1)

        # User input validation
        while value == 0:
            print("The name you entered cannot be found, please try again. If you don't remember the name you entered, "
                  "please quit the program by entering \"quit\".")
            name1 = input().strip()
            if name1 == "quit":
                print("Thank you for using HomeMed!")
                quit()
            print("Please enter the new number.")
            number1 = input().strip()
            value = db1.update(name1, number1)

        print("Your information has been updated!")

    if choice == "a":
        print("Please enter the name associated with the number you would like to see. *Case sensitive")
        name = input().strip()
        db1 = Database('db.txt')
        value = db1.select(name)

        # User input validation
        while value == 0 and name != "quit":
            print("The name you entered cannot be found, please try again. If you don't remember the name you "
                  "entered, please quit the program by entering \"quit\".")
            name = input().strip()
            value = db1.select(name)
        if name == "quit":
            print("Thank you for using HomeMed!")
            quit()
        print(value)

    if choice == "q":
        break


print("Thank you for using HomeMed!")



