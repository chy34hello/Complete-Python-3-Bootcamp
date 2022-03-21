# EDIT THE FILE WITH YOUR SOLUTION
import sys
import re


#FILE_NAME = input('Which text file do you want to use for the puzzle?')
FILE_CONTENTS = 'test_3.txt'
DELIMITERS = '\.|\?|\!'

STATEMENT_pattern = r'"([A-Za-z0-9_\./\\-]*)"'

try:
  with open(FILE_CONTENTS,'r') as f:
    FILE_CONTENTS= f.read()
except FileNotFoundError:
  print(f"No such file or directory:{FILE_CONTENTS}")


list1 = re.split(DELIMITERS,FILE_CONTENTS.replace('\n', ' ').replace('!"', '"!').replace('."', '".').replace(',"', '",').strip())
list1.pop()
print(list1)

print()
print()

SirList = dict()
for s in list1:
  if 'Sir ' in s and '"' in s:
    before, key, name2 = s.partition('Sir ')
    name2 = name2.split(' ')[0]

    m = s.split('"')[1]
    if 'Sir ' in m:
      before, key, name = m.partition('Sir ')
      name = name.split(' ')[0]
      if name.strip() not in SirList.keys():
        SirList[name.strip()] = ''
    SirList[name2.strip()] = m
  elif  'Sir ' in s and '"' not in s:
      before, key, name2 = s.partition('Sir ')
      name2 = name2.split(' ')[0]
      if name.strip() not in SirList.keys():
        SirList[name.strip()] = ''

  if 'Sirs' in s:
    before, key, names = s.partition('Sirs')
    namesList = names.split(',')
    for name in namesList:
      if ' and ' in name:
        before, key, name = name.partition(' and ')
        SirList[before.strip()] = ''
        SirList[name.strip()] = ''
      else:
        SirList[name.strip()] = ''


print(SirList)
sortedSirs = dict(sorted(SirList.items()))
print(sortedSirs.keys())


#GENERATING all possiblities for each Sir
intToDigits = lambda a : list(map(int, str(a)))
   
Sirs_num = len(SirList)
formating_String = str(0)+str(Sirs_num)+'b'
initialP =[]
for p in range(2**Sirs_num):
  temp = [(int(c)) for c in f'{p:{formating_String}}']
  initialP.append(temp)

print(initialP)