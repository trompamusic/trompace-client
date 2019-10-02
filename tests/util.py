import os


def read_file(dirname, filename):
    with open(os.path.join(dirname, filename)) as fp:
        return fp.read()
