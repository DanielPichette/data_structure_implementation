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
