import bz2
import regex
from wget import download

from src.data import get_db_filepath, get_names_filepath


def download_database(year, month):
    filename = "lichess_db_standard_rated_{}-{:02d}.pgn.bz2".format(year, month)
    url = "https://database.lichess.org/standard/{}".format(filename)
    download(url, out=get_db_filepath(year, month))


def _get_name(line):
    m = regex.match("\[(White|Black) \"(.+)\"\]", line)
    name = None
    try:
        name = m[2]
    except TypeError:
        pass
    return name


def process_database(year, month):
    names = set()
    with open(get_names_filepath(year, month), 'w+') as namesf:
        with bz2.BZ2File(get_db_filepath(year, month)) as f:
            for line in f:
                n = _get_name(line.decode('utf-8'))
                if n is not None and n not in names:
                    names.add(n)
                    namesf.write("{}\n".format(n))


def main():
    pass
    # download_database(2020, 4)
    # process_database(2020, 4)


if __name__ == "__main__":
    main()
