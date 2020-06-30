from src.data.ranking_file import read
from src.data.rankings import get_and_save_rankings
from src.data.raw import save_names_from_database
from src.ranking.calculation import get_user_ranking
from src.ranking.differences import calculate_ranking_difference_across_variants
from src.ranking.uncertain import fill_uncertain_values
from src.utils.filenames import get_ranking_filename
from src.ranking.fide import Regression, filter_rankings_by_fide


def main():
    # save_names_from_database(2020, 4)
    # get_and_save_rankings(2020, 4)

    # calculate_ranking_difference_across_variants(read(get_ranking_filename(2020, 4)), 2020, 4)
    filled_rankings = fill_uncertain_values(read(get_ranking_filename(2020, 4)), 2020, 4)

    filled_filtered_rankings = filter_rankings_by_fide(filled_rankings)

    regression = Regression.calculate(filled_filtered_rankings)
    print(regression)


if __name__ == "__main__":
    main()