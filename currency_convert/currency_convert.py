with open('data.csv', 'r') as input_data:
    data_lines = [line.rstrip() for line in input_data]

results = []
for line in data_lines:
    words = line.split(',')
    listOfFloat = map(float, words[1:])
    tup = (words[0], listOfFloat)
    results.append(tup)
print(results)