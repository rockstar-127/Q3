from Sorting_Package.src.sorting_algorithms import SortingSelector

def read_entire_file(filepath):
    """Reads the entire content of a file into a single string."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None

def validate_input(data):
    try :
        data = list(map(int, data))
    except :
        raise TypeError("Input must be a list.")
    
    if len(data) >= 2 * 10**5:
        raise ValueError("List size must be < 2 × 10^5.")

    for x in data:
        if not isinstance(x, int):
            raise TypeError("All elements must be integers.")

def main():
    file_data = read_entire_file('input.txt')
    if file_data:
        lines = file_data.strip().split("\n")
        try : 
            data = list(lines[0].strip().split()) 
        except :
            print('Error conversion : using default data/list')
            data = [5, 1, 3, 2, 4]
    else :
        print('Error Empty File : using default data/list')
        data = [5, 1, 3, 2, 4]
    
    validate_input(data)
    
    algo = "quick"
    sorter = SortingSelector(algo)

    print(f"Using {algo} sort:")
    print("Original:", data)
    print("Ascending:", sorter.sort(data, "ascending"))
    print("Descending:", sorter.sort(data, "descending"))

if __name__ == "__main__":
    main()
