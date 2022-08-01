import os
import random

dates = []

def gen_date(max_commits, counter = 0):
    while counter <= max_commits:
        year = random.randint(2021, 2022)
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        counter = counter + 1
        date = f"{year}-{month}-{day}"
        dates.append(date)
                    
def make_commits():
    for date in dates:
        print(date)
        os.system(f"echo {date} > commits.yml")
        os.system(f"git add commits.yml")
        os.system(f'git commit -m "{date}" --date "{date}" > dates.log')
    os.system('git push')

def main():
    gen_date(20000)
    make_commits()

if __name__ == '__main__':
    main()
