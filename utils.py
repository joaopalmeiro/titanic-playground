def truncate_number(n, decimals=2):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
