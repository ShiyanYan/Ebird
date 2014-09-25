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
	if float(ss[LatiIndex])>LatiMax: LatiMax = float(ss[LatiIndex])
	if float(ss[LatiIndex])<LatiMin: LatiMin = float(ss[LatiIndex])
	if float(ss[LongtiIndex])>LongMax: LongMax = float(ss[LongtiIndex])
	if float(ss[LongtiIndex])<LongMin: LongMin = float(ss[LongtiIndex])

print "LatiMax:",LatiMax,"LatiMin:",LatiMin
print "LongMax:",LongMax,"LongMin:",LongMin
