import os
import random
from datetime import date
week = random.randint(0, 54)
day = random.randint(0, 6)

date = date.today() 


#date = os.system('echo $(date)')
#date = 'sex 7 Dec 2022 18:41:45'

print(date)

#os.system(f'echo ${date} > commits.yml')
#os.system('git add commits.yml')
#os.system(f'git commit -m "${date}" --date "${date}"')
#os.system('git push')

