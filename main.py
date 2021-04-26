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

calss:
