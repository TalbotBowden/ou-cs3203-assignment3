def sum_of_list(numbers):
    return sum(numbers)

def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  # Convert strings to integers

    total = sum_of_list(numbers)
    product_total = product_of_list(numbers)

    print(f"Sum: {total}")
    print(f"Product: {product_total}")

    reversed_numbers = reverse_list(numbers)
    print(f"Reversed: {reversed_numbers}")


if __name__ == "__main__":
    main()

def reverse_list(numbers):
    return numbers[::-1]
#new comment lol
