from src.api_token import get_token
from src.db import process_database
from src.rankings import process_rankings, get_user_ranking
from src.regression import calculate_regression


def main():
    # process_database(2020, 4)
    # process_rankings(2020, 4)
    r = calculate_regression(2020, 4)
    print(r)

    token = get_token()
    rank = get_user_ranking('Lukasz1928', token, r)
    print(rank)


if __name__ == "__main__":
    main()