Tiny script to repair fixed gear speed from cadence data. 

Usage:
    1. using GoldenCheetah export activity as CSV file. Activity -> Export... 
    2. python fix_speed /tmp/no_speed.csv /tmp/fixed_speed.csv
    3. using GoldenCheetah import activity from fixed CSV file. Activity -> Import from file...
    4. using GildenCheetah export fixed activity to .FIT file: Activity -> Export... 
        choose fixed.fit as destination.
    5. upload fixed.fit to strava.com or other service you need.

`
usage: fixed gear speed resolver [-h] [--tyre-circumference CIRCUMFERENCE]
                                 [--chainring-size CHR_TEETH] [--cog COG]
                                 csv out_csv

positional arguments:
  csv                   file with activity
  out_csv               result csv file with corrected speed & cadence

optional arguments:
  -h, --help            show this help message and exit
  --tyre-circumference CIRCUMFERENCE, -c CIRCUMFERENCE
                        tyre circumference in mm, default is 2096 for 700x23c
                        tyre
  --chainring-size CHR_TEETH, -r CHR_TEETH
                        number of chainring teeth, default=52
  --cog COG, -g COG     cog size. number of teeth, default=14
  `
