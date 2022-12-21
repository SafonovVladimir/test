def get_leaders(numbers: list) -> list:
    numbers.append(0)
    return [numbers[i] for i in range(len(numbers) - 1) if numbers[i] > sum(numbers[i + 1:])]



print(get_leaders([16, 17, 4, 3, 5, 2]))
print(get_leaders([1, 2, 3, 4, 0]))