import csv
import operator
d = {}
with open('try4.txt', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        d[row[1]] = row[0:]
#print(d)

res=max(d.iteritems(), key=operator.itemgetter(1))[0]
print (res)


