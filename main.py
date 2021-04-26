import random

# PROBLEM 1
# choose the best data structure (between a dictionary, set, or tuple) to efficiently store the data.
# A : Store the months of the year. Grab the month in which Pi Day exists and print it to the console.
# tuple because the months are set, and cant be changed.

months_in_a_year = (
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november')
pi_day = 'march'


def find_month(desired_month):
    for individual_month in months_in_a_year:
        if desired_month == individual_month:
            print(desired_month)
            break


find_month(pi_day)

# B : Store all of the locations where you have celebrated your birthday.
birthday_location = {'disney world', 'movies', 'club', 'home', 'aquarium'}
# Add three locations where you may celebrate your birthday in the future.
birthday_location.update(['six flags', 'beach', 'camp ground'])
# Iterate over the collection and print each one to the console.
for location in birthday_location:
    print(location)

# C : Store sweepstakes contestants. Since a sweepstakes is a competition that contains a winner, there must be a way
# to uniquely identify each contestant
# Dictionary data structure

contestant1 = {'first_name': 'Lyra', 'last_name': 'Parker'}
contestant2 = {'first_name': 'Dez', 'last_name': 'Sanchez'}
contestant3 = {'first_name': 'River', 'last_name': 'Smith'}
contestant4 = {'first_name': 'Liza', 'last_name': 'Heinz'}
contestant5 = {'first_name': 'Leo', 'last_name': 'Flor'}


class Sweepstakes:

    def __init__(self):
        self.contestants = [contestant1, contestant2, contestant3, contestant4, contestant5]
        self.winner = self.select_winner()

    def select_winner(self):
        self.winner = random.choice(self.contestants)
        return self.winner


sweepstakes = Sweepstakes()
print(sweepstakes.winner)


# PROBLEM 2
# Use a list to store the dictionary of your immediate family members, with each index of the list storing
# its own dictionary


