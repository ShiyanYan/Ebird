#Recode the checklists to Region, Season, Species, ChecklistNum of Obeservers, Completeness
import cPickle as pickle
inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")

MinLong = 60
MaxLong = 130

MinLati = 20
MaxLati = 50



tempPath = "/home/projects/ebird/BCR30/Temp/"

ObserIDdic = pickle.load(tempPath + "UserIDCount.dump")
EventIDdic = pickle.load(tempPath + "EventIDCount.dump")

newdic = []
for item in sorted(ObserIDdic):
	newdic[item] = ObserIDdic[item]
ObserIDdic = dict(newdic)

newdic = []
for item in sorted(EventIDdic):
	newdic[item] = EventIDdic[item]
EventIDdic = dict(newdic)



previous = ""

LatiIndex = 0
LongtiIndex = 0
DateIndex = 0
CompleteIndex = 0
SEIndex = 0
ObserIndex = 0

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
		continue
	EventID = ss[SEIndex]
	if EventID == previous: continue
	cline = EventID + ","

	Lati = float(ss[LatiIndex])
	Long = float(ss[LongtiIndex])
	k1 = int((Lati - 20)/0.25)
	k2 = int((Long + 130)/0.25)
	Region = str(k1 * 1000 + k2)
	cline = cline + Region + ','

	Date = ss[ObserIndex]
	month = int(Date.split("-")[1])
	mnumber = 0
	if (month>=1) and (month<=2):
		mnumber = 1
	elif (month>=3) and (month<=5):
		mnumber = 2
	elif (month>=6) and (month<=8):
		mnumber = 3
	elif (month>=9) and (month<=10):
		mnumber = 4
	else:
		mnumber = 1
	cline = cline + str(mnumber) + ","

	SpecNum = EventIDdic[EventID]
	cline = cline + str(SpecNum) + ","

	Obserlevel = ObserIDdic[ss[ObserIndex]]
	cline = cline + str(Obserlevel) + ","

	Complete = ss[CompleteIndex]

	cline = cline + Complete + "\n"
	previous = EventID
	lineset.append(cline)

lineset = sorted(lineset)

previous = ""
newlineset = []
for line in lineset:
	if line == previous: continue
	newlineset.append(line)
	previous = line

outputHeadLine = "EventID,Region,Season,SpeciesNum,ObserverLevel,Completeness\n"
outputfile = open("/home/projects/ebird/BCR30/EBD_Encoded_5var.csv","w")
outputfile.write(outputHeadLine)
for line in newlineset:
	outputfile.write(line)

