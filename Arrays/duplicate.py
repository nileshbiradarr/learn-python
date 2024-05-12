def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    unique_numbers = remove_duplicates(numbers)
    print("Numbers after removing duplicates:", unique_numbers)
