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

# Sort the two lists. 
list_one.sort()
list_two.sort()

# Compare smallest location ID in left list with smallest in right, and so on to find the total distance between the locations.
total_distance = 0
for i, item in enumerate(list_one):
    # print(f'Index {i}: Compare {item} to {list_two[i]}')
    total_distance += abs(int(item) - int(list_two[i]))
    # print(total_distance)

print(f'The total distance is {total_distance}.')

# The correct answer to Part 1 is 2344935.
