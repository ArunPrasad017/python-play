import json
import csv
with open("data.json") as file:
    data=json.load(file)
columns = [x for x in data.keys()]
with open("data.csv","w") as f:
    csv_file = csv.writer(f)
    csv_file.writerow(columns)
    for row in data:
        print(row)
        temp = print(data[row])
        csv_file.writerow(temp)