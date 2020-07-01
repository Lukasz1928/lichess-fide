from src.utils.variants import variants


def has_established_ranking_in_variant(player, variant):
    return player[variant][1] <= 90


def has_established_ranking_in_variants(player, variant_list):
    return all([has_established_ranking_in_variant(player, variant) for variant in variant_list])


def get_player_ranking_in_variant(player, variant):
    if variant == 'fide':
        return player['fide']
    return player[variant][0]


def split_variants_by_established(player):
    established = []
    provisional = []
    for variant in variants:
        if has_established_ranking_in_variant(player, variant):
            established.append(variant)
        else:
            provisional.append(variant)
    return established, provisional
