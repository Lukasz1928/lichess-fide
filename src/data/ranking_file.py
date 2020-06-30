from src.utils.variants import variants

_values_in_file = variants + ['rd_' + v for v in variants] + ['fide']


def _format_line(ranking):
    rank_list = [ranking[v][0] for v in variants] + [ranking[v][1] for v in variants] + [ranking['fide']]
    return ("{}," * len(_values_in_file))[:-1].format(*rank_list)


def _parse_line(line):
    values = [int(v) if v != "None" else None for v in line[:-1].split(',')]
    ranks = {}
    for i, v in enumerate(variants):
        ranks[v] = (values[i], values[i + len(variants)])
    ranks['fide'] = values[len(variants)]
    return ranks


def save(rankings, filename):
    exists = True
    try:
        open(filename, 'r').close()
    except FileNotFoundError:
        exists = False
    with open(filename, 'a+') as f:
        if not exists:
            f.write(",".join(_values_in_file) + "\n")
        for r in rankings:
            f.write(_format_line(r) + "\n")


def read(filename):
    ranks = []
    with open(filename, 'r') as f:
        f.__next__()
        for line in f:
            ranks.append(_parse_line(line))
    return ranks
