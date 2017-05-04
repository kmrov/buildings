import csv

from normalize import normalize_address

housedata = {
    normalize_address(row[3]): row
    for row in
    csv.reader(open("data/housedata.csv"))
}

renovation = [b.strip() for b in open("data/list2.txt").readlines()]

notfound_f = open("data/notfound.txt", "w")
found_wr = csv.writer(open("data/found.csv", "w"))

found_wr.writerow(["ADDR"] + next(csv.reader(open("data/housedata.csv"))))

for building in renovation:
    data = housedata.get(normalize_address(building), None)
    if data is None:
        data = housedata.get(normalize_address(building + ", стр. 1"), None)
    if data is None:
        print(building, file=notfound_f)
    else:
        found_wr.writerow([building] + data)
