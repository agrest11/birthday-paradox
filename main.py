import datetime
import random


def get_birthdays(number_of_birthdays):
    birthdays = []

    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2000, 12, 31)

    # calculate number of days needed
    num_days = (end_date - start_date).days

    # generate random dates
    for i in range(0, number_of_birthdays):
        rand_days = random.randint(1, num_days)
        random_date = start_date + datetime.timedelta(days=rand_days)
        random_date = random_date.strftime("%d-%B")
        birthdays.append(random_date)

    return birthdays


def get_match(received):
    # check if there are repeated birthdays
    if len(received) == len(set(received)):
        return None

    # compare each birthday to any other birthday
    for a, birthdayA in enumerate(received):
        for b, birthdayB in enumerate(received[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


def simulation(number_of_birthdays):
    print(f'\nGenerating {number_of_birthdays} random birthdays 100,000 times...')
    sim_match = 0
    for i in range(100000):
        birthdays = get_birthdays(number_of_birthdays)
        matched = get_match(birthdays)
        if matched is not None:
            sim_match += 1

    return sim_match


def main():
    # get number of birthdays to draw
    number_of_birthdays = input('Enter the number of birthdays: ')
    # enter the number until it's a valid value
    while not number_of_birthdays.isdecimal() or int(number_of_birthdays) > 100:
        number_of_birthdays = input('Enter the number of birthdays: ')
    number_of_birthdays = int(number_of_birthdays)

    # generate birthdays and display them
    received_birthdays = get_birthdays(number_of_birthdays)
    print(f'Drawn birthdays in this simulation:')
    for i, birthday in enumerate(received_birthdays):
        if i != 0:
            print(', ', end='')
        print(birthday, end='')

    # check if there are any matching birthdays in the group
    matched = get_match(received_birthdays)
    if matched is not None:
        print(f'\n\nRepeated birthday: {matched}')
    else:
        print(f'\n\nAll birthdays are unique!')

    # run 100,000 simulations
    simulation_match = simulation(number_of_birthdays)
    # calculate probability of several people having birthday on the same day
    probability = round(simulation_match / 100000 * 100, 2)

    # display simulation results
    print(f'\nOut of 100,000 simulations of {number_of_birthdays} people, there was a')
    print(f'matching birthday in that group {simulation_match} times. This means')
    print(f'that {number_of_birthdays} people have a {probability} % chance of')
    print('having a matching birthday in their group.')


if __name__ == '__main__':
    main()

# probability = round(simMatch / 100000 * 100, 2)
