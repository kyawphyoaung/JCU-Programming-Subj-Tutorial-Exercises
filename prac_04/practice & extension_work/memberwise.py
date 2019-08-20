results = []
def main():
    results = add_memberwise([1, 2, 3], [4, 5, 6, 7])
    print(results)

def add_memberwise(first_nums, second_nums):
    first_nums = [int(i) for i in first_nums]
    second_nums = [int(i) for i in second_nums]
    for i, j in zip(first_nums, second_nums):
        result = i+j
        results.append(result)
    return results

main()