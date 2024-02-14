def stats_decorator(func):
    def wrapper(line):
        numbers = list(map(float, line.strip().split()))
        count = len(numbers)
        average = sum(numbers) / count
        maximum = max(numbers)

        print(f"Numbers read: {numbers}")
        print(f"Count of numbers: {count}")
        print(f"Average of numbers: {average:.2f}")
        print(f"Maximum of numbers: {maximum}")

        # original function call
        func(line)

    return wrapper

@stats_decorator
def process_line(line):
    pass

def printStats(t):
    """Read data from file and then calls the decorator for each line."""
    with open(t, 'r') as file:
        for line in file:
            process_line(line)


text_file = 'no.txt'
printStats(text_file)
