import csv

# Open the dataset file
fileh=open('ratings.csv','r')
# List of people
people=list()
# Dictionary  for people's ratings
ratings=dict()

reader = csv.reader(fileh, delimiter=',')
l=list()
# For every line in the file
for row in reader:
	l=row
	if l[0] not in people:
		people.append(l[0])
		ratings[l[0]]={}
	ratings[l[0]][l[1]]=float(l[2])