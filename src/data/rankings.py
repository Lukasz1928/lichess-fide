import asyncio
import os
from time import sleep

from lichess_client import APIClient

from src.data.ranking_file import save
from src.utils.api_token import get_token
from src.utils.filenames import get_names_filepath, get_ranking_filename
from src.utils.misc import slice_array
from src.utils.variants import variants


async def _request_rankings(token, names):
    client = APIClient(token)
    r = await client.users.get_users_by_id(names)
    return r.entity


def _get_rankings(token, names):
    wait_time = 1
    while True:
        response = asyncio.run(_request_rankings(token, names))
        status = response.code
        print(status)
        if status != 429:
            break
        sleep(60 * wait_time + 1)
        wait_time += 1
    return response


def _extract_rankings(player):
    fide = None
    try:
        fide = player['profile']['fideRating']
    except KeyError:
        pass
    ranks = {'fide': fide}
    for variant in variants:
        variant_data = player['perfs'][variant]
        ranks[variant] = (variant_data['rating'], variant_data['rd'])
    return ranks


def get_and_save_rankings(year, month):
    names_filename = get_names_filepath(year, month)
    with open(names_filename, 'r') as f:
        names = [n.strip('\n') for n in f]
    names_chunk_size = 1000
    token = get_token()
    try:
        os.remove(get_ranking_filename(year, month))
    except FileNotFoundError:
        pass  # no such file
    for names_chunk in slice_array(names, names_chunk_size):
        rankings_response = _get_rankings(token, names_chunk)
        players = rankings_response.content
        print(len(players), len(names_chunk))
        rankings = [_extract_rankings(p) for p in players]
        save(rankings, get_ranking_filename(year, month))
