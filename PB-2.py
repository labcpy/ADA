from itertools import combinations

def find_subsets_with_sum(S, target_sum):
    result = []
    for subset_length in range(1, len(S) + 1):
        for subset in combinations(S, subset_length):
            if sum(subset) == target_sum:
                result.append(subset)

    return result

S = [1, 2, 5, 6, 8]
target_sum = 9


subsets_with_sum = find_subsets_with_sum(S, target_sum)

if not subsets_with_sum:
    print("No subset with the given sum")
else:
    print("Subsets with the given sum:", subsets_with_sum)

