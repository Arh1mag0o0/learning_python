def merge(values):      # values - это список словарей
    out = {}
    for i in values:
        for j in i:
            if j not in out:
                out[j] = {i[j], }
            else:
                out[j].add(i[j])
    return out




