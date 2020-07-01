

def save_processed(names, filename):
    with open(filename, 'a+') as f:
        for name in names:
            f.write(name + "\n")


def read_processed(filename):
    names = set()
    try:
        with open(filename, 'r') as f:
            for name in f:
                names.add(name)
    except FileNotFoundError:
        pass
    return names
