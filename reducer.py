import fileinput

transactions_count = 0
totalpayout = 0

for line in fileinput.input():

    data = line.strip().split("\t")    

    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    current_key, current_value = data

    transactions_count += 1
    totalpayout += float(current_value)

print transactions_count, "\t", totalpayout
