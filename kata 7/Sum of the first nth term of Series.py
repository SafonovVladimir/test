def series_sum(n):
    if n == 0:
        return '0.00'
    result = 1
    count = 1
    dev = 4
    while count < n:
        result += 1 / dev
        count += 1
        dev += 3
    return '{:.2f}'.format(result)


# print(series_sum(1))
# print(series_sum(2))
print(series_sum(3))
