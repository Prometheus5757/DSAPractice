def compare_versions(version1, version2):
    """Compares two version strings (X.Y.Z) by converting them to tuples of integers."""
    return tuple(map(int, version1.split('.'))) < tuple(map(int, version2.split('.')))

def merge_sorted_lists(*lists):
    """Merges multiple sorted lists without using a heap."""
    k = len(lists)  # Number of lists
    indices = [0] * k  # Track positions in each list
    result = []

    while True:
        min_version = None
        min_list_idx = -1

        # Find the smallest available version
        for i in range(k):
            if indices[i] < len(lists[i]):  # Check if the list has remaining elements
                current_version = lists[i][indices[i]]
                if min_version is None or compare_versions(current_version, min_version):
                    min_version = current_version
                    min_list_idx = i

        # If no version was found, all lists are exhausted
        if min_list_idx == -1:
            break
        
        # Add the smallest version to the result
        result.append(min_version)
        indices[min_list_idx] += 1  # Move pointer forward in that list

    return result

# Example usage
list1 = ["1.0.0", "1.2.3", "1.3.0"]
list2 = ["1.2.0", "1.3.4", "2.0.0"]
list3 = ["1.2.5", "2.1.0"]

merged_list = merge_sorted_lists(list1, list2, list3)
print(merged_list)