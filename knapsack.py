#
# Simple Python implementation of 0/1 Knapsack problem.
# Kasey Stowell
#

# initialize vals
weight = 50
wt = [15, 25, 45, 30, 23, 37]
val = [100, 350, 225, 67, 275, 168]
numitems = 6
table = [[0] * (weight + 1) for x in range(numitems + 1)]
knapsack = []

#  fill table..
for i in range(1, numitems + 1):
    for w in range(1, weight + 1):
        if wt[i - 1] > w:
            table[i][w] = table[i - 1][w]
        elif wt[i - 1] <= w:
            if table[i - 1][w] > (val[i - 1] + table[i - 1][w - wt[i - 1]]):
                        table[i][w] = table[i - 1][w]
            else:
                table[i][w] = val[i - 1] + table[i - 1][w - wt[i - 1]]

# visual helper
print("Your table...")
print("----------")
for row in range(numitems + 1):
    print(table[row])
print("----------")

# fill knapsack!
i = numitems
w = weight
while i > 0 and w > 0:
    if table[i][w] != table[i - 1][w]:
        knapsack.append([i, wt[i - 1], val[i - 1]])
        w = w - wt[i - 1]
        i = i - 1
    else:
        i = i - 1

print("Your knapsack inventory!")
print("----------")
# visual helper
for item in knapsack:
    print(item)
print("----------")