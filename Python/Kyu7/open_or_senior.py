def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append('Senior')
        else:
            result.append('Open')

    return result


print(open_or_senior(
    [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
