from src.data.download import download_database
from src.data.ranking_file import read_rankings
from src.data.rankings import get_and_save_rankings
from src.data.raw import save_names_from_database
from src.ranking.differences import calculate_ranking_difference_across_variants, save_ranking_differences
from src.ranking.uncertain import fill_and_filter_uncertain_values
from src.utils.filenames import get_ranking_filename
from src.ranking.fide import Regression, filter_rankings_by_fide


def _save_results(ranking_differences, regression):
    save_ranking_differences(ranking_differences, '../docs_src/public/ranking-differences.json')
    regression.save('../docs_src/public/regression.json')


def main():
    year, month = 2020, 4

    # download_database(year, month)
    # save_names_from_database(year, month)
    # get_and_save_rankings(year, month)

    rankings = read_rankings(get_ranking_filename(year, month))
    ranking_differences = calculate_ranking_difference_across_variants(rankings)
    filled_rankings = fill_and_filter_uncertain_values(rankings, ranking_differences)

    filled_filtered_rankings = filter_rankings_by_fide(filled_rankings)

    regression = Regression.calculate(filled_filtered_rankings)

    _save_results(ranking_differences, regression)


if __name__ == "__main__":
    main()
