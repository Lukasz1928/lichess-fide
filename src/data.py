
def get_db_filename(year, month):
    return 'db-{}-{:02d}.pgn.bz2'.format(year, month)


def get_db_filepath(year, month):
    return '../data/{}'.format(get_db_filename(year, month))


def get_names_filepath(year, month):
    return '../data/names-{}-{:02d}.txt'.format(year, month)


def get_ranking_filepath(year, month):
    return '../data/rankings-{}-{:02d}.csv'.format(year, month)


def get_ranking_partial_location():
    return '../data/temp'


def get_ranking_partial_filename(id):
    return '{}/{}.csv'.format(get_ranking_partial_location(), id)

