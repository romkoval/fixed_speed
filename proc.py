import csv

total_dist=0.0
with open('trak.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in spamreader:
        dist_km = int(row[3]) / 60 * 52/14 * 2.095 / 1000
        speed = "%.2f" % (dist_km * 3600)
        total_dist += dist_km
        row[1] = "%.5f" % total_dist
        row[5] = speed
        print('\t'.join(row))
