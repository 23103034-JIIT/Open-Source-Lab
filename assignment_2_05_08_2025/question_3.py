def find_duplicates(integers):
    seen = set()
    duplicates = set()
    
    for number in integers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    
    return list(duplicates)

integers = [1, 1, 2, 2, 3, 3, 4, 4, 5]
print(find_duplicates(integers))