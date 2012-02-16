def progressprinter(iterable, every=1000):
    length = len(iterable)
    for i, row in enumerate(iterable):
        if i % every == 0:
            print i, 'of', length, row
        yield row
