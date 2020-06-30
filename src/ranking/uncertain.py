from src.ranking.differences import read_ranking_differences
from src.ranking.utils import split_variants_by_established, get_player_ranking_in_variant
from src.utils.filenames import get_ranking_differences_filename


def _fill_provisional_rankings(player, ranking_differences):
    established, provisional = split_variants_by_established(player)
    if len(established) == 0:
        return None
    rankings = {k: player[k][0] for k in established}
    for prov in provisional:
        expecteds = []
        for est in established:
            expected_for_prov = get_player_ranking_in_variant(player, est) + ranking_differences[est][prov]
            expecteds.append(expected_for_prov)
        rankings[prov] = sum(expecteds) / len(expecteds)
    rankings['fide'] = get_player_ranking_in_variant(player, 'fide')
    return rankings


def fill_uncertain_values(rankings, year, month):
    ranking_differences = read_ranking_differences(get_ranking_differences_filename(year, month))
    filled = [_fill_provisional_rankings(p, ranking_differences) for p in rankings]
    return [f for f in filled if f is not None]
