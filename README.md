Tiny script to repair fixed gear speed from cadence data. 

Usage:

    * using GoldenCheetah export activity as CSV file. Activity -> Export... 
    * use this script to fix missing or incorrect speed data:
         python fix_speed.py /tmp/no_speed.csv /tmp/fixed_speed.csv
    * using GoldenCheetah import activity from fixed CSV file. Activity -> Import from file...
    * using GildenCheetah export fixed activity to .FIT file: Activity -> Export... 
        choose fixed.fit as destination.
    * upload fixed.fit to strava.com or other service you need.

```
usage: fixed gear speed resolver [-h] [--tyre-circumference CIRCUMFERENCE]
                                 [--chainring-size CHR_TEETH] [--cog COG]
                                 csv out_csv

positional arguments:
  csv                   file with activity
  out_csv               result csv file with corrected speed & distance

optional arguments:
  -h, --help            show this help message and exit
  --tyre-circumference CIRCUMFERENCE, -c CIRCUMFERENCE
                        tyre circumference in mm, default is 2096 for 700x23c
                        tyre
  --chainring-size CHR_TEETH, -r CHR_TEETH
                        number of chainring teeth, default=52
  --cog COG, -g COG     cog size. number of teeth, default=14
  ```
