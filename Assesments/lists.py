def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return (result)
my_list = [2, 3, 2, 4, 5, 3, 6, 7, 5]

print(remove_duplicates(my_list))
