from src.data.rankings import get_and_save_rankings
from src.data.raw import save_names_from_database
from src.ranking.calculation import get_user_ranking


def main():
    # save_names_from_database(2020, 4)
    get_and_save_rankings(2020, 4)
    # r = calculate_regression(2020, 4)
    # print(r)
    # print(r.score)

    # token = get_token()
    # rank = get_user_ranking('Lukasz1928', token, r)
    # print(rank)


if __name__ == "__main__":
    main()