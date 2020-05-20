from src.data import get_names_filepath, get_ranking_filepath
from lichess_client import APIClient
import asyncio
from src.api_token import get_token


async def get_rankings(token, names):
    client = APIClient(token)
    r = await client.users.get_users_by_id(names)
    return r.entity.content


def get_player_rankings(player):
    rankings = {}
    fide = player['profile']['fideRating']
    rankings['fide'] = (fide, None)
    perfs = player['perfs']
    game_types = ['bullet', 'blitz', 'rapid', 'classical', 'correspondence']
    for gt in game_types:
        r, c = perfs[gt]['rating'], perfs[gt]['games']
        rankings[gt] = (r, c)
    return rankings


def has_fide_ranking(player):
    try:
        _ = player['profile']['fideRating']
    except Exception:
        return False
    return True

def process_rankings(year, month):
    # names_filename = get_names_filepath(year, month)
    # with open(names_filename, 'r') as f:
    #     names = [n for n in f]
    names = ['hpy']
    token = get_token()
    response = asyncio.run(get_rankings(token, names))
    players = [p for p in response if has_fide_ranking(p)]
    for player in players:
        rankings = get_player_rankings(player)
        print(rankings)



    # with open(get_ranking_filepath(year, month)) as f:

process_rankings(0, 0)