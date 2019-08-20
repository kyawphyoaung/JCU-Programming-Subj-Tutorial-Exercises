numbers = [3, 1, 4, 1, 5, 9, 2]

def warmup():
    print(numbers) #[3, 1, 4, 1, 5, 9, 2]
    print(numbers[0]) #3
    print("-1 result ", numbers[-1]) #2
    print("-2 result ", numbers[-2]) #9
    print("3 result ",numbers[3]) #1
    print(":-1 result ", numbers[:-1]) #[3, 1, 4, 1, 5, 9]
    print("3:4 result ",numbers[3:4]) #[1]
    print("5 in result ", 5 in numbers) #True
    print("7 in result ", 7 in numbers) #False
    print("3" in numbers) #False
    print(numbers + [6, 5, 3]) #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

def expression():
    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers)
    print(numbers[2:])
    print(9 in numbers)

expression()