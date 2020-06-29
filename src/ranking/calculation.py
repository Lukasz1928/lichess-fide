import os
from math import ceil
from time import sleep

from src.utils.filenames import get_names_filepath, get_ranking_filename, get_ranking_partial_location
from lichess_client import APIClient
import asyncio
from src.utils.api_token import get_token


async def get_rankings(token, names):
    client = APIClient(token)
    r = await client.users.get_users_by_id(names)
    return r.entity


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


def format_save_line(rank):
    return "{},{},{},{},{},{},{}\n".format(rank['name'], rank['rankings']['fide'][0],
                                           rank['rankings']['bullet'][0],
                                           rank['rankings']['blitz'][0], rank['rankings']['rapid'][0],
                                           rank['rankings']['classical'][0],
                                           rank['rankings']['correspondence'][0])


def save_rankings(year, month):
    partial_files = os.listdir(get_ranking_partial_location())
    partial_files.remove('.gitkeep')
    with open(get_ranking_filename(year, month), 'w+') as f:
        f.write("name,fide,bullet,blitz,rapid,classical,correspondence\n")
        for pf in partial_files:
            with open('{}/{}'.format(get_ranking_partial_location(), pf)) as partial:
                for l in partial:
                    f.write(l)


def save_partial_rankings(rankings, id):
    with open('{}/{}.csv'.format(get_ranking_partial_location(), id), 'w+') as f:
        for r in rankings:
            f.write(format_save_line(r))


def read_done_chunks():
    return len(os.listdir(get_ranking_partial_location())) - 1





async def aget_user_ranking(user, token):
    client = APIClient(token)
    r = await client.users.get_users_by_id([user])
    return r


def get_user_ranking(user, token, regression):
    response = asyncio.run(aget_user_ranking(user, token))
    p = response.entity.content[0]['perfs']
    ranks = p['bullet']['rating'], p['blitz']['rating'], p['rapid']['rating'], \
            p['classical']['rating'], p['correspondence']['rating']
    return regression(ranks)


def process_rankings(year, month):
    names_filename = get_names_filepath(year, month)
    with open(names_filename, 'r') as f:
        names = [n.strip('\n') for n in f]
    names_chunk_size = 20000
    token = get_token()
    total_requests = ceil(float(len(names)) / names_chunk_size)
    for id, names_chunk in enumerate(slice_array(names, names_chunk_size)):
        rankings = []
        done_chunks = read_done_chunks()
        if id < done_chunks:
            continue
        wait_time = 1
        while True:
            response = asyncio.run(get_rankings(token, names_chunk))
            status = response.code
            if status != 429:
                # print('success {}/{} ({}/{} players)'.format((id + 1), total_requests, (id + 1) * names_chunk_size, len(names)))
                break
            print('waiting for {} minute(s)'.format(wait_time))
            sleep(60 * wait_time + 1)
            wait_time += 1

        response = response.content
        players = [p for p in response if has_fide_ranking(p)]
        ranks = [p['perfs'] for p in players]
        print(ranks)
    #     for player in players:
    #         player_rankings = get_player_rankings(player)
    #         rankings.append({'name': player['id'],
    #                          'rankings': player_rankings})
    #     save_partial_rankings(rankings, id)
    #
    # save_rankings(year, month)