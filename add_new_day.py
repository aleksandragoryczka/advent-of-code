import os

year_nr = '2025'
day_nr = '01'

os.mkdir(f"{year_nr}/day{day_nr}")
open(f"{year_nr}/day{day_nr}/task01.py", "w")
open(f"{year_nr}/day{day_nr}/task02.py", "w")

os.mkdir(f"{year_nr}/inputs/day{day_nr}")
open(f"{year_nr}/inputs/day{day_nr}/test.txt", "w")
open(f"{year_nr}/inputs/day{day_nr}/input.txt", "w")
