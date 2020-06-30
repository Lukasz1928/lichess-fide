import json

from src.utils.filenames import get_ranking_differences_filename
from src.utils.variants import variants


def _get_player_raking_in_variant(player, variant):
    return player[variant][0]


def _has_established_ranking_in_variant(player, variant):
    return player[variant][1] <= 90


def _has_established_ranking_in_variants(player, variant_list):
    return all([_has_established_ranking_in_variant(player, variant) for variant in variant_list])


def calculate_ranking_difference_across_variants(rankings, year, month):
    differences = {v1: {v2: 0.0 for v2 in variants} for v1 in variants}
    for i1, variant1 in enumerate(variants):
        for i2, variant2 in enumerate(variants):
            if i1 < i2:
                ranking_diff_sum = 0
                count = 0
                for player in rankings:
                    if _has_established_ranking_in_variants(player, [variant1, variant2]):
                        ranking_diff_sum += _get_player_raking_in_variant(player, variant2) - _get_player_raking_in_variant(player, variant1)
                        count += 1
                differences[variant1][variant2] = ranking_diff_sum / count
                differences[variant2][variant1] = -ranking_diff_sum / count
    save_ranking_differences(differences, get_ranking_differences_filename(year, month))


def save_ranking_differences(ranking_differences, filename):
    str_rd = str(ranking_differences)
    with open(filename, 'w+') as f:
        f.write(str_rd)


def read_ranking_differences(filename):
    with open(filename, 'r') as f:
        str_rd = f.read()
    return json.loads(str_rd)