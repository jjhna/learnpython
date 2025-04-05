numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
i = 3
newlist = [numbers[i] for i in range(len(numbers)) if numbers[i] >= 0]
print(newlist)