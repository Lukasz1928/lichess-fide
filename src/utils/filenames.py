
def get_db_filename_without_path(year, month):
    return 'db-{}-{:02d}.pgn.bz2'.format(year, month)


def get_db_filename(year, month):
    return '../data/{}'.format(get_db_filename_without_path(year, month))


def get_names_filename(year, month):
    return '../data/names-{}-{:02d}.txt'.format(year, month)


def get_ranking_filename(year, month):
    return '../data/rankings-{}-{:02d}.csv'.format(year, month)


def get_partial_processed_filename():
    return '../data/processed.txt'
