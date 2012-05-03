def progressprinter(iterable, every=1):
	""" Prints a progress counter like "1 of 1000" . """
    length = len(iterable)
    for i, row in enumerate(iterable):
        if i % every == 0:
            print i, 'of', length, row
        yield row

def main(func):
	""" Decorator which evokes the function if the script was run from the commandline """
	if __name__ == '__main__':
		func()
	return func