from src.sorting_algorithms import SortingSelector
def test_all_sorts():
    sample = [5, 3, 1, 4, 2]
    expected_asc = [1, 2, 3, 4, 5]
    expected_desc = [5, 4, 3, 2, 1]

    for algo in ["bubble", "selection", "quick", "merge"]:
        sorter = SortingSelector(algo)
        assert sorter.sort(sample, "ascending") == expected_asc
        assert sorter.sort(sample, "descending") == expected_desc

if __name__ == "__main__":
    test_all_sorts()
    print("All tests passed!")
