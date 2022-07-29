import os

Y = 2004
M = 6
D = 4

os.system(f'git commit -m commits.yml --date ${Y}-${M}-${D}:10:57-03:00')
os.system('git add .')
os.system('git push -u origin main')
