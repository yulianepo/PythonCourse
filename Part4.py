    import collections

    db = collections.defaultdict(list)
    with open('words.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            key = "".join(sorted(line.strip('\n')))
            #db[key] = line.strip('\n')
            db[key].append(line.strip('\n'))

    print(db)
