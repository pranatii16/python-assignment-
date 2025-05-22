def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # recursively flatten
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, [5, 6]]]
print("Flattened list:", flatten(nested_list))