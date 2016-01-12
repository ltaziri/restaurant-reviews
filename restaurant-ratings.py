import sys

# file_name = sys.argv[1]

def rate_restaurant():
    """Print out restaurants with its rating.

    data_file is derived from the command line, input 
    after the script(restaurant-ratings.py).

    Example:

    $python restaurant-ratings.py scores.txt

    """

    data_file = open(sys.argv[1])

    restaurant_score = {}

    for line in data_file:
        line = line.rstrip()
        res_rating = line.split(":")
        key = res_rating[0]
        value = res_rating[1]
        restaurant_score[key] = value


    restaurant_keys = sorted(restaurant_score)

    for res in restaurant_keys:
        print res, "is rated at", restaurant_score[res] + '.'


    data_file.close()

rate_restaurant()

