def split_iterable(iterable, q):
    n = len(iterable)
    i = counter = 0
    while i < n:
        if not counter:
            iterable.append(list())
        if counter < q:
            iterable[-1].append(iterable.pop(0))
            i += 1
            counter += 1
        else:
            counter = 0
    return iterable
