#LongLatiRangeCalc.py
# count the scope of latitude and longtitudes
inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")
tt = 0
LongMax = -200
LongMin = 200
LatiMax = -200
LatiMin = 200
for line in inputfile:
	ss = line.split("\t")
	tt += 1
	if tt==1:
	    width = len(ss)
	    for i in range(0,width):
	    	if ss[i] == "LATITUDE": latiIndex = i
	    	if ss[i] == "LONGTITUDE": LongtiIndex = i
	    	if ss[i] == "OBSERVATION DATE": ObserIndex = i
	    	if ss[i] == "ALL SPECIES REPORTED": CompleteIndex = i
	    continue
	if int(ss[latiIndex])>LatiMax: LatiMax = int(ss[latiIndex])
	if int(ss[latiIndex])<LatiMin: LatiMin = int(ss[latiIndex])
	if int(ss[LongtiIndex])>LongMax: LongMax = int(ss[LongtiIndex])
	if int(ss[LongtiIndex])<LongMin: LongMin = int(ss[LongtiIndex])