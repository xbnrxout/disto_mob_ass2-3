import timeit
code_to_test = """
from io import StringIO
import csv
from functools import reduce
from multiprocessing import Pool


f =  open('./sequential-map-reduce/FullData.csv')
soccer_list = f.read().split(',')

mapper = len

def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c

def chunkify(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk) 
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)

data_chunks = chunkify(soccer_list, 30)

mapped = map(chunks_mapper, data_chunks)

reduced = reduce(reducer, mapped)


print(reduced)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print("Sequential Processing")
print(elapsed_time)