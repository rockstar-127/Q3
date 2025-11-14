from src.sorting_algorithms import SortingSelector
def main():
    data = [5, 1, 3, 2, 4]
    algo = "quick"

    sorter = SortingSelector(algo)

    print(f"Using {algo} sort:")
    print("Original:", data)
    print("Ascending:", sorter.sort(data, "ascending"))
    print("Descending:", sorter.sort(data, "descending"))

if __name__ == "__main__":
    main()
