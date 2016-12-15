import zipfile
import cStringIO
from urllib import urlopen

DATA_URL = 'http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip'


def zip_extract():
    """
    Generator that:
        Extracts by downloading the csv.zip, unzipping.
        Transforms the data into python via CSV lib
        Loads it to the end user as a python list
    """

    f = urlopen(DATA_URL)
    buf = cStringIO.StringIO(f.read())
    zfile = zipfile.ZipFile(buf)
    buf = cStringIO.StringIO(zfile.read('top-1m.csv'))
    for line in buf:
        (rank, domain) = line.split(',')
        yield (int(rank), domain.strip())


def top_list(num=100):
    a = zip_extract()
    return [a.next() for x in xrange(num)]


if __name__ == "__main__":
    print top_list()