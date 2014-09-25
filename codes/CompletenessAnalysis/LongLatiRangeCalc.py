#LongLatiRangeCalc.py
# count the scope of latitude and longtitudes
inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")
tt = 0
LongMax = -200
LongMin = 200
LatiMax = -200
LatiMin = 200
LatiIndex = 0
LongtiIndex = 0
ObserIndex = 0
CompleteIndex = 0

outputfile = open("/home/projects/ebird/BCR30/EBD_Encoded.csv","w")

headline = "Region,Month,Complete\n"
outputfile.write(headline)

for line in inputfile:
	ss = line.split("\t")
	tt += 1
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "LATITUDE": LatiIndex = i
			if ss[i] == "LONGITUDE": LongtiIndex = i
			if ss[i] == "OBSERVATION DATE": ObserIndex = i
			if ss[i] == "ALL SPECIES REPORTED": CompleteIndex = i
		continue

	Lati = ss[LatiIndex]
	Long = ss[LongtiIndex]
	Date = ss[ObserIndex]
	Complete = ss[CompleteIndex]
	k1 = 0
	k2 = 0
	if Lati<39:
		k1 = 1
	elif lati<41:
		k1 = 2
	elif lati<43:
		k1 = 3
	else:
		k1 = 4

	if Long<-82:
		k2 = 1
	elif Long<-78:
		k2 = 2
	elif Long<-74:
		k2 = 3
	else:
		k2 = 4

	rnumber = (k1-1)*4 + k2
	month = int(Date.split("-")[1])
	mnumber = 0
	if (month>=1) and (month<=3):
		mnumber = 1
	elif (month>=4) and (month<=6):
		mnumber = 2
	elif (month>=7) and (month<=9):
		mnumber = 3
	elif (month>=10) and (month<=11):
		mnumber = 4
	else:
		mnumber = 1

	outputfile.write("rnumber" + "," + "mnumber" + "," + Complete + "\n")




	# if float(ss[LatiIndex])>LatiMax: LatiMax = float(ss[LatiIndex])
	# if float(ss[LatiIndex])<LatiMin: LatiMin = float(ss[LatiIndex])
	# if float(ss[LongtiIndex])>LongMax: LongMax = float(ss[LongtiIndex])
	# if float(ss[LongtiIndex])<LongMin: LongMin = float(ss[LongtiIndex])

print "LatiMax:",LatiMax,"LatiMin:",LatiMin
print "LongMax:",LongMax,"LongMin:",LongMin
