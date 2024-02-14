import matplotlib.pyplot as plt

def graphSnowfall(t):
    snowfall_ranges = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0}

    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            for key in snowfall_ranges.keys():
                lower, upper = map(int, key.split('-'))
                if lower <= snowfall <= upper:
                    snowfall_ranges[key] += 1
                    break

    ranges = list(snowfall_ranges.keys())
    counts = list(snowfall_ranges.values())

    plt.bar(ranges, counts, color='blue')
    plt.xlabel('Snowfall Range (in cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()

#Example:
text_file = 'abc.txt'
graphSnowfall(text_file)
