import os
import random
from datetime import date

counter = 0

actual_date = date.today().strftime("%Y-%m-%d")


while counter <= 1000:
    year = random.randint(2021, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    print(f"{year}-{month}-{day}")

    os.system(f'echo {year}-{month}-{day} > commits.yml')
    os.system('git add commits.yml')
    os.system(f'git commit -m "{year}-{month}-{day}" --date "{year}-{month}-{day}"')
    counter = counter + 1

os.system('git push')
