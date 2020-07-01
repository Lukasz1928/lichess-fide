from src.ranking.utils import has_established_ranking_in_variants, get_player_ranking_in_variant
from src.utils.variants import variants


def calculate_ranking_difference_across_variants(rankings):
    differences = {v1: {v2: 0.0 for v2 in variants} for v1 in variants}
    for i1, variant1 in enumerate(variants):
        for i2, variant2 in enumerate(variants):
            if i1 < i2:
                ranking_diff_sum = 0
                count = 0
                for player in rankings:
                    if has_established_ranking_in_variants(player, [variant1, variant2]):
                        ranking_diff_sum += get_player_ranking_in_variant(player, variant2) - get_player_ranking_in_variant(player, variant1)
                        count += 1
                differences[variant1][variant2] = ranking_diff_sum / count
                differences[variant2][variant1] = -ranking_diff_sum / count
    return differences
