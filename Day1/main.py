# Day 1: Historian Hysteria

# Read input data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Separate the data into two lists
list_one = []
list_two = []

for row in data:
    list_one.append(row.split(' ')[0])
    list_two.append(row.split(' ')[-1])

# Part One:
def PartOne():
    # Sort the two lists. 
    list_one.sort()
    list_two.sort()

    # Compare smallest location ID in left list with smallest in right, and so on to find the total distance between the locations.
    total_distance = 0
    for i, item in enumerate(list_one):
        total_distance += abs(int(item) - int(list_two[i]))

    print(f'The total distance is {total_distance}.')
    # The correct answer to Part One is 2344935.

# Part Two:
# Similarity score = the Location ID in List One * the number of times it appears in List Two.
def PartTwo(list_one, list_two):
    total_similarity_score = 0
    for i, location in enumerate(list_one):
        number = int(location)
        appearances = 0
        similarity_score = 0
        for j, comparison in enumerate(list_two):
            if int(comparison) == number:
                appearances += 1
            similarity_score = int(location) * appearances
        total_similarity_score += similarity_score
    print(total_similarity_score)

    # The correct answer to Part Two is 27647262.

PartTwo(list_one, list_two)