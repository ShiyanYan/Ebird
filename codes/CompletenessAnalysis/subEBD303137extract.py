import cPickle as pickle

indic = open("/home/projects/ebird/BCR30/ObMatchSY.dump","r")
ObMatchSY = pickle.load(indic)

infile = open("/home/projects/ebird/BCR30/ECR303137.txt","r")


commonSpecies = ["northern cardinal","american robin","mourning dove","american crow","blue jay","tufled titmouse","common grackle","house sparrow","white-throated sparrow","gray catbird","black-capped chickadee","house finch","white-breasted nuthatch","rock pigeon","dark-eyed junco","american tree sparrow","common eider","piping plover","common raven","american woodcock"]

rareSpecies = ["swamp sparrow","indigo bunting","blue-gray gnatcatcher","black vulture","forster's tern","northern parula","purple martin","white-eyed vireo","blackpoll warbler","blue grosbeak","winter wren","royal tern","american pipit","yellow-breasted chat","yellow-throated vireo","louisiana waterthrush","brown-headed nuthatch"]


outfile = open("/home/projects/ebird/BCR30/SubEBD303137-TruncHis.csv","w")
outfile.write("EventID,ObserverID,Complete,SYear,BCR,Common,Rare,Count,SpecNum\n")

ObserIndex = 0
DateIndex = 0
CompleteIndex = 0
SEIndex = 0
BCRIndex = 0
ObserCountIndex = 0
ComNameIndex = 0
SciNameIndex = 0
SubComNameIndex = 0
SubSciNameIndex = 0
base = 0
previous = ""
commoncount = 0
rarecount = 0
totCount = 0
SpeciesCount = 0
tt = 0
Year = 0
UserID = ""
BCR = ""
Complete = ""
for line in infile:
	ss = line.split("\t")
	tt += 1
	#if tt>100000: break
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "OBSERVER ID": ObserIndex = i
			if ss[i] == "OBSERVATION DATE": DateIndex = i
			if ss[i] == "ALL SPECIES REPORTED": CompleteIndex = i
			if ss[i] == "SAMPLING EVENT IDENTIFIER": SEIndex = i
			if ss[i] == "BCR CODE": BCRIndex = i
			if ss[i] == "OBSERVATION COUNT": ObserCountIndex = i
			if ss[i] == "COMMON NAME": ComNameIndex = i
			if ss[i] == "SCIENTIFIC NAME": SciNameIndex = i 
			if ss[i] == "SUBSPECIES COMMON NAME": SubComNameIndex = i
			if ss[i] == "SUBSPECIES SCIENTIFIC NAME": SubSciNameIndex = i
		continue
	Year = int(ss[DateIndex][0:4])
	if Year < 2002: continue
	EventID = ss[SEIndex]
	if tt==2: previous = EventID
	if (EventID!=previous) and (previous!=""):
		if ObMatchSY[UserID] < 2002: 
			base = 2002
		else:
			outfile.write(previous + "," + UserID + "," + Complete + ",")
			base = ObMatchSY[UserID]
			outfile.write(str(yearprevious - base + 1) + "," + BCR + "," + str(commoncount) + "," + str(rarecount) + "," + str(totCount) + "," + str(SpeciesCount) + "\n")
			if (yearprevious-base<0): print UserID,yearprevious,ObMatchSY[UserID]
		commoncount = 0
		rarecount = 0
		totCount = 0
		SpeciesCount = 0
	previous = EventID
	yearprevious = Year
	UserID = ss[ObserIndex]
	Complete = ss[CompleteIndex]
	BCR = ss[BCRIndex]
	Count = ss[ObserCountIndex]
	if Count!="X": totCount += int(Count)
	if (ss[ComNameIndex].lower() in commonSpecies) or (ss[SciNameIndex].lower() in commonSpecies) or (ss[SubComNameIndex].lower() in commonSpecies) or (ss[SubSciNameIndex].lower() in commonSpecies):
		commoncount += 1
	if (ss[ComNameIndex].lower() in rareSpecies) or (ss[SciNameIndex].lower() in rareSpecies) or (ss[SubComNameIndex].lower() in rareSpecies) or (ss[SubSciNameIndex].lower() in rareSpecies):
		rarecount += 1
	SpeciesCount += 1

outfile.write(EventID + "," + UserID + "," + Complete + ",")
if ObMatchSY[UserID] < 2002: 
	base = 2002
else:
	base = ObMatchSY[UserID]
outfile.write(str(Year - base + 1) + "," + BCR + "," + str(commoncount) + "," + str(rarecount) + "," + str(totCount) + "," + str(SpeciesCount) + "\n")
	
	
