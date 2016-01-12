import sys

# file_name = sys.argv[1]

restaurant_score = {}

def print_restaurant_score(restaurant_dict):

    restaurant_keys = sorted(restaurant_dict)

    for res in restaurant_keys:
        print "{} is rated at {}.".format(res, restaurant_score[res])


def rate_restaurant():
    """Print out restaurants with its rating.

    data_file is derived from the command line, input 
    after the script(restaurant-ratings.py).

    Example:

    $python restaurant-ratings.py scores.txt

    """

    data_file = open(sys.argv[1])


    for line in data_file:
        line = line.rstrip()
        res_rating = line.split(":")
        restaurant = res_rating[0]
        score = int(res_rating[1])
        restaurant_score[restaurant] = score


    print_restaurant_score(restaurant_score)


    data_file.close()

rate_restaurant()

choice = raw_input("Do you want to add a new restaurant? Y/N")

if choice[0] == 'Y' or choice[0] == 'y':
    new_restaurant = raw_input("Enter the restaurant name. ")
    new_score = int(raw_input('Rate this restaurant on a scale of 0 - 5. '))
    restaurant_score[new_restaurant] = new_score
    print_restaurant_score(restaurant_score)
else:
    print "Thank you and bye!"



