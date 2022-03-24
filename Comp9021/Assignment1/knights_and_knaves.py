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


#print(SirList)
sortedSirs = dict(sorted(SirList.items()))
# print(list(sortedSirs.keys()))
print(sortedSirs)


#GENERATING all possiblities for each Sir
intToDigits = lambda a : list(map(int, str(a)))
   
Sirs_num = len(SirList)
formating_String = str(0)+str(Sirs_num)+'b'
initialP =[]
for p in range(2**Sirs_num):
  temp = [(int(c)) for c in f'{p:{formating_String}}']
  initialP.append(temp)

print(initialP)



def conjunction_of_sirs(sentence):
  if ' and ' in sentence.lower():
    return True
  else:
    return False
  
def disjunction_of_sirs(sentence):
  if ' or ' in sentence.lower():
    return True
  else:
    return False

def rule_1(sentence):
  least = True if re.search(r'\bleast\b', sentence.lower()) else False
  us = True if re.search(r'\bus\b', sentence.lower()) else False
  return least and (conjunction_of_sirs(sentence.lower()) or us)

def rule_2(sentence):
  most = True if re.search(r'\bmost\b', sentence.lower()) else False
  us = True if re.search(r'\bus\b', sentence.lower()) else False
  return most and (conjunction_of_sirs(sentence.lower()) or us)

def rule_3(sentence):
  exactly = True if re.search(r'\bexactly\b', sentence.lower()) else False
  us = True if re.search(r'\bus\b', sentence.lower()) else False
  return exactly and (conjunction_of_sirs(sentence.lower()) or us)

def rule_4(sentence):
  are = True if re.search(r'\bare\b', sentence.lower()) else False
  all = True if re.search(r'\ball\b', sentence.lower()) else False
  return are and all

def rule_5(sentence):
  am = True if re.search(r'\bam \b', sentence.lower()) else False
  I = True if re.search(r'\bi \b', sentence.lower()) else False
  return am and I

def rule_6(sentence):
  sir = True if re.search(r'\bsir \b', sentence.lower()) else False
  _is = True if re.search(r'\b is \b', sentence.lower()) else False
  noOr = False if re.search(r'\b or\b', sentence.lower()) else True
  return sir and noOr and _is

def rule_7(sentence):
  _is = True if re.search(r'\b is \b', sentence.lower()) else False
  return _is and disjunction_of_sirs(sentence.lower())

def rule_8(sentence):
  are = True if re.search(r'\bare\b', sentence.lower()) else False
  return are and conjunction_of_sirs(sentence.lower())
  



def whichRule(sentence):
  if rule_1(sentence) == True:
      return 1
  elif rule_2(sentence) == True:
      return 2
  elif rule_3(sentence) == True:
      return 3
  elif rule_4(sentence) == True:
      return 4
  elif rule_5(sentence) == True:
      return 5
  elif rule_6(sentence) == True:
      return 6
  elif rule_7(sentence) == True:
      return 7  
  elif rule_8(sentence) == True:
      return 8  

#print(whichRule('I am a Knave'))

def biconditional(p,q):
  if p==True and q==True:
    return True
  elif p==False and q==False:
    return True
  else:
    return False


def parsingSirs(sentense):
  l1 = list()
  sentense = sentense.replace(',','')
  splited = sentense.split(' ')
  for i in range(0, len(splited)):
    if splited[i]=='Sir' or splited[i]=='sir':
      l1.append(splited[i+1])
  if "I " in sentense:
    l1.append('I')
  return l1


print(parsingSirs('Sir Nancy and I are Knaves'))

#sortedSirs , initialP
#list(sortedSirs.keys())
keys = list(sortedSirs.keys())
print(keys)



#execute rule:

def run_rule_5(is_knight, sentense):
  value =is_knight if 'knight' in sentense.lower() else not is_knight
  return biconditional(is_knight, value )

def run_rule_8(speaker,posibility, sentense):
  value= True
  # extract Sirs list 
  sirs_involved = parsingSirs(sentense)
  for i in range(0, len(sirs_involved)):
    if sirs_involved[i] == "I":
      sirs_involved[i] = speaker

  for sir in sirs_involved:
    index = keys.index(sir)
    if ' knights' in sentense.lower():
      if posibility[index]==0:
        value =False
    elif ' knaves' in sentense.lower():
      if posibility[index]==1:
        value = False
  
  s_index = keys.index(speaker)
  speaker_is_night = True if posibility[s_index] ==1 else False

  return biconditional(speaker_is_night, value )



#print(run_rule_8('Andrew',[0,0,0,0], 'Sir Nancy and I are Knaves'))





def true_false(num):
  return True if num else False





Result = False

def truth_table():
  for posibility in initialP:
    for i in range (len(sortedSirs)):

      # to implement 2 or more statements
      if(sortedSirs[keys[i]]):
        if (whichRule(sortedSirs[keys[i]])==5):
          Result = run_rule_5(true_false(posibility[i]),sortedSirs[keys[i]])
        elif (whichRule(sortedSirs[keys[i]])==8):
          print('Rule 8 is triggered')
          Result = run_rule_8( keys[i],posibility,sortedSirs[keys[i]])
        if Result:
          print(posibility)
  Result = False


truth_table()
