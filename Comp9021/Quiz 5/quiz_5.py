import csv


all_rows = list()

class row:
    def __init__(self, id, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio):
        self.id = id
        self.objective = objective(age, gender, height, weight)
        self.examination = examination(ap_hi, ap_lo, cholesterol, gluc)
        self.subjective = subjective(smoke, alco, active, cardio)

class objective:
    def __init__(self, age, gender, height, weight):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

class examination:
    def __init__(self, ap_hi, ap_lo, cholesterol, gluc):
        self.ap_hi = ap_hi
        self.ap_lo = ap_lo
        self.cholesterol = cholesterol
        self.gluc = gluc

class subjective:
    def __init__(self, smoke, alco, active, cardio):
        self.smoke = smoke
        self.alco = alco
        self.active = active
        self.cardio = cardio

def apply_ignore_records_filter(obj, exam):
    filter_1 = int(obj.height) >= 150 and int(obj.height) <= 200
    filter_2 = float(obj.weight) >= 50.0 and float(obj.weight) <= 150
    filter_3 = int(exam.ap_hi) >=80   and int(exam.ap_hi) <=200
    filter_4 = int(exam.ap_lo) >=70 and int(exam.ap_lo) <=140
    filter_applied = filter_1 and filter_2 and filter_3 and filter_4
    return filter_applied


def age_filter(obj, age):
    return int(int(obj.age)/365) == age

def gender_filter(obj, gender):
    return int(obj.gender) == gender


def max_min_value(all_rows):
    height =list()
    weight = list()
    ap_hi = list()
    ap_lo = list()

    for record in all_rows:
        height.append(int(record.objective.height))
        weight.append(float(record.objective.weight))
        ap_hi.append(int(record.examination.ap_hi))
        ap_lo.append(int(record.examination.ap_lo))
    
    print(max(height),  min(height))
    print(max(weight),  min(weight))
    print(max(ap_hi),  min(ap_hi))
    print(max(ap_lo),  min(ap_lo))


with open('cardio_train.csv', 'r') as f:
    csv_reader = csv.reader(f,delimiter =";")
    next(csv_reader)
 

    for line in csv_reader:
        record = row(*tuple(line))
        if  apply_ignore_records_filter(record.objective, record.examination)and age_filter(record.objective,43) and gender_filter(record.objective, 2):
            all_rows.append(record) 

    print(len(all_rows))
    max_min_value(all_rows)



