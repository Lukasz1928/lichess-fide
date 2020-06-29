import bz2
import regex

from src.utils.filenames import get_db_filepath, get_names_filepath


def _get_name(line):
    m = regex.match("\[(White|Black) \"(.+)\"\]", line)
    name = None
    try:
        name = m[2]
    except TypeError:
        pass
    return name


def save_names_from_database(year, month):
    names = set()
    with open(get_names_filepath(year, month), 'w+') as namesf:
        with bz2.BZ2File(get_db_filepath(year, month)) as f:
            for line in f:
                n = _get_name(line.decode('utf-8'))
                if n is not None and n not in names:
                    names.add(n)
                    namesf.write("{}\n".format(n))
