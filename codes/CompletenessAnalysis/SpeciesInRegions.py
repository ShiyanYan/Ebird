#SpeciesInRegions
import cPickle as pickle
inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")

MinLong = 60
MaxLong = 130

MinLati = 20
MaxLati = 50

regionList = [79219,77213,77214,75220,76212,75213]

tempPath = "/home/projects/ebird/BCR30/Temp/"

ObserIDdic = pickle.load(open(tempPath + "UserIDCount.dump","r"))
EventIDdic = pickle.load(open(tempPath + "EventIDCount.dump","r"))

newdic = {}
for item in sorted(ObserIDdic):
	newdic[item] = ObserIDdic[item]
ObserIDdic = dict(newdic)

newdic = {}
for item in sorted(EventIDdic):
	newdic[item] = EventIDdic[item]
EventIDdic = dict(newdic)



previous = ""


speciesDicC = {}
speciesDicA = {}

subspeciesDicC = {}
subspeciesDicA = {}

LatiIndex = 0
LongtiIndex = 0
DateIndex = 0
CompleteIndex = 0
SEIndex = 0
ObserIndex = 0
tt = 0
lineset = []
for line in inputfile:
	ss = line.split("\t")
	tt += 1
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "LATITUDE": LatiIndex = i
			if ss[i] == "LONGITUDE": LongtiIndex = i
			if ss[i] == "OBSERVATION DATE": DateIndex = i
			if ss[i] == "ALL SPECIES REPORTED": CompleteIndex = i
			if ss[i] == "SAMPLING EVENT IDENTIFIER": SEIndex = i
			if ss[i] == "OBSERVER ID": ObserIndex = i
			if ss[i] == "SCIENTIFIC NAME": SpeciesIndex = i
			if ss[i] == "SUBSPECIES SCIENTIFIC NAME": SubspeciesIndex = i
		continue
	EventID = ss[SEIndex]

	Lati = float(ss[LatiIndex])
	Long = float(ss[LongtiIndex])
	k1 = int((Lati - 20)/0.25)
	k2 = int((Long + 130)/0.25)
	if not (k1 * 1000 + k2) in regionList: continue

	sciName = ss[SpeciesIndex]
	subSciName = ss[SubspeciesIndex]
	Complete = ss[CompleteIndex]
	if sciName in speciesDicA:
		speciesDicA[sciName] += 1
	else:
		speciesDicA[sciName] = 1

	if subSciName in subspeciesDicA:
		subspeciesDicA[subSciName] += 1
	else:
		subspeciesDicA[subSciName] = 1

	if Complete=="1":
		if sciName in speciesDicC:
			speciesDicC[sciName] += 1
		else:
			speciesDicC[sciName] = 1	

		if subSciName in subspeciesDicC:
			subspeciesDicC[subSciName] += 1
		else:
			subspeciesDicC[subSciName] = 1


outputHeadLine = "SpeciesSciName,InCompleteness,Completeness\n"
outputfile = open("/home/projects/ebird/BCR30/SpeciesCompleteness.csv","w")
outputfile.write(outputHeadLine)
for sp in speciesDicA:
	outputfile.write(sp + ",")
	if sp in speciesDicC:
		outputfile.write( str(speciesDicA[sp]-speciesDicC[sp])+ "," + str(speciesDicC[sp]) + "\n")
	else:
		outputfile.write( "0" + "," + str(speciesDicA[sp]) + "\n")

outputHeadLine = "SubSpeciesSciName,InCompleteness,Completeness\n"
outputfile2 = open("/home/projects/ebird/BCR30/SubSpeciesCompleteness.csv","w")
outputfile2.write(outputHeadLine)
for sp in subspeciesDicA:
	outputfile2.write(sp + ",")
	if sp in subspeciesDicC:
		outputfile2.write( str(subspeciesDicA[sp]-subspeciesDicC[sp])+ "," + str(subspeciesDicC[sp]) + "\n")
	else:
		outputfile2.write( "0" + "," + str(subspeciesDicA[sp]) + "\n")