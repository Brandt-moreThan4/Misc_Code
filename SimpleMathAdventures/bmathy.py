"""Bunch of random math functions that may be useful at some point?"""
import matplotlib.pyplot as plt


def is_factor(number, potential_factor):
    """Test for if arg 2 is a factor of arg 1"""

    if number % potential_factor == 0:
        return True
    else:
        return False


def factors(integer, show_negatives=False):
    """Returns a list of all the factors of the provided integer"""

    if integer < 0:
        return None

    all_factors = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            all_factors.append(i)

    if show_negatives:
        all_factors.extend([i * -1 for i in all_factors])

    return all_factors


def multiplication_table(number, multiple_ceiling=10):
    """Prints a multiplication table up to ceiling. 10 is default"""

    for i in range(multiple_ceiling + 1):
        print(f'{number} x {i} = {number * i:.2f} ')


def frange(start, stop, increment):
    """List of floating point numbers"""
    numbers = []
    while start < stop:
        numbers.append(start)
        start += increment
    return numbers


def force_between(mass1, mass2, distance):
    """Calculate attractive force between two objects"""

    # Gravitational Constant
    G = 6.674 * (10 ** -11)
    return (G * mass1 * mass2) / distance ** 2


def plot_force_change_by_distance(mass1=10, mass2=10):
    """Plot graph of force between two body's changing by distance"""

    distances = range(100, 1001, 50) # In meters I think
    forces = []

    for distance in distances:
        forces.append(force_between(mass1, mass2, distance))

    plt.style.use('seaborn')
    plt.plot(distances, forces)
    plt.xlabel('Distance in Meters')
    plt.ylabel('Force in Newtons')
    plt.title('Gravitational Force between objects with mass1: ' + str(mass1) + '  and mass2:' + str(mass2))
    plt.show()


def variance(number_list):
    """Population variance of a list of numbers"""
    x_bar = sum(number_list) / len(number_list)
    sum_of_squares = sum([(x - x_bar) ** 2 for x in number_list])
    return sum_of_squares / len(number_list)


def correlation(x_vals, y_vals):
    """Return pearson correlation coefficient given two lists of numbers."""

    n = len(x_vals)
    x_bar = sum(x_vals) / n
    y_bar = sum(y_vals) / n

    numerator = 0
    for x, y in zip(x_vals, y_vals):
        numerator += (x - x_bar) * (y - y_bar)

    #covariance below
    numerator = numerator/n

    x_sigma = variance(x_vals)**.5
    y_sigma = variance(y_vals)**.5
    return numerator / (x_sigma * y_sigma)
