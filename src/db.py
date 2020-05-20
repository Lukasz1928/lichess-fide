import bz2
import regex
from wget import download


def _get_db_filename(year, month):
    return 'db-{}-{:02d}.pgn.bz2'.format(year, month)


def _get_db_filepath(year, month):
    return '../data/{}'.format(_get_db_filename(year, month))


def _get_names_filepath(year, month):
    return '../data/names-{}-{:02d}.txt'.format(year, month)


def download_database(year, month):
    filename = "lichess_db_standard_rated_{}-{:02d}.pgn.bz2".format(year, month)
    url = "https://database.lichess.org/standard/{}".format(filename)
    download(url, out=_get_db_filepath(year, month))


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
    with open(_get_names_filepath(year, month), 'w+') as namesf:
        with bz2.BZ2File(_get_db_filepath(year, month)) as f:
            for line in f:
                n = _get_name(line.decode('utf-8'))
                if n is not None and n not in names:
                    names.add(n)
                    namesf.write("{}\n".format(n))


def main():
    # download_database(2020, 4)
    process_database(2020, 4)


if __name__ == "__main__":
    main()
