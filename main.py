# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106000299.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
# target_data = data[:10]
target_data = []
humd1 = 0
humd2 = 0
humd3 = 0
humd4 = 0
humd5 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
length = len(data)
index = 0
for i in range(length):
    if (data[i]['station_id'] == 'C0A880'):
        count1 = count1 + 1
        if (data[i]['HUMD'] == '-99.000') or (data[i]['HUMD'] == '-999.000'):
            flag1 = flag1 + 1
        else:
            humd1 = humd1 + float(data[i]['HUMD'])
    elif (data[i]['station_id'] == 'C0F9A0'):
        count2 = count2 + 1
        if (data[i]['HUMD'] == '-99.000') or (data[i]['HUMD'] == '-999.000'):
            flag2 = flag2 + 1
        else:
            humd2 = humd2 + float(data[i]['HUMD'])
    elif (data[i]['station_id'] == 'C0G640'):
        count3 = count3 + 1
        if (data[i]['HUMD'] == '-99.000') or (data[i]['HUMD'] == '-999.000'):
            flag3 = flag3 + 1
        else:
            humd3 = humd3 + float(data[i]['HUMD'])
    elif (data[i]['station_id'] == 'C0R190'):
        count4 = count4 + 1
        if (data[i]['HUMD'] == '-99.000') or (data[i]['HUMD'] == '-999.000'):
            flag4 = flag4 + 1
        else:
            humd4 = humd4 + float(data[i]['HUMD'])
    elif (data[i]['station_id'] == 'C0X260'):
        count5 = count5 + 1
        if (data[i]['HUMD'] == '-99.000') or (data[i]['HUMD'] == '-999.000'):
            flag5 = flag5 + 1
        else:
            humd5 = humd5 + float(data[i]['HUMD'])

if (count1 == flag1): target_data.append(['C0A880', 'None'])
else: target_data.append(['C0A880', humd1])
if (count2 == flag2): target_data.append(['C0F9A0', 'None'])
else: target_data.append(['C0F9A0', humd2])
if (count3 == flag3): target_data.append(['C0G640', 'None'])
else: target_data.append(['C0G640', humd3])
if (count4 == flag4): target_data.append(['C0R190', 'None'])
else: target_data.append(['C0R190', humd4])
if (count5 == flag5): target_data.append(['C0X260', 'None'])
else: target_data.append(['C0X260', humd5])

#=======================================

# Part. 4
#=======================================
# Print result
target_data.sort()
print(target_data)
#========================================