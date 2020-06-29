from wget import download

from src.utils.filenames import get_db_filepath


def download_database(year, month):
    filename = "lichess_db_standard_rated_{}-{:02d}.pgn.bz2".format(year, month)
    url = "https://database.lichess.org/standard/{}".format(filename)
    download(url, out=get_db_filepath(year, month))
