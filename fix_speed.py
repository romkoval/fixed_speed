import csv
import argparse
from argparse import FileType

def main(args):
    total_dist=0.0
    with open(args.csv, newline='') as csvfile:
        activity = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        fields = activity.fieldnames
        if 'cad' not in fields:
            raise Exception('cad not in cvs header')
        if 'kph' not in fields:
            fields += 'kph'
        if 'km' not in fields:
            fields += 'km'
        writer = csv.DictWriter(args.out_csv, fieldnames=fields)
        writer.writeheader()
        
        for row in activity:
            
            dist_km = int(row['cad']) / 60 * args.chr_teeth/args.cog * (args.circumference/1000) / 1000
            speed = "%.2f" % (dist_km * 3600)
            total_dist += dist_km
            row['km'] = "%.5f" % total_dist
            row['kph'] = speed
            writer.writerow(row)
            


if __name__ == "__main__":
    args = argparse.ArgumentParser("fixed gear speed resolver")
    args.add_argument("--tyre-circumference", "-c", dest="circumference", 
                      default="2096", type=int,
                      help="tyre circumference in mm, default is %(default)s for 700x23c tyre")
    args.add_argument("--chainring-size", "-r", dest="chr_teeth", type=int,
                      default="52",
                      help="number of chainring teeth, default=%(default)s")
    args.add_argument("--cog", "-g", dest="cog", type=int, 
                      default="14",
                      help="cog size. number of teeth, default=%(default)s")

    args.add_argument("csv", help="file with activity")
    args.add_argument("out_csv", type=FileType(mode="w"), 
                       help="result csv file with corrected speed & cadence")
    
    main(args.parse_args())
