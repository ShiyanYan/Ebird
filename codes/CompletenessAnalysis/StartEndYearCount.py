#Count the start year for every observer
import cPickle as pickle
infile = open("/home/projects/ebird/BCR30/ECR303137.txt","r")

dic = {}

ObMatchSY = {}  # observer ID match start year
ObMatchEY = {} #  observer ID match end year
tt = 0
ObserIndex = 0
DateIndex = 0
for line in infile:
	ss = line.split("\t")
	tt += 1
	#if tt>2000: break
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "OBSERVER ID": ObserIndex = i
			if ss[i] == "OBSERVATION DATE": DateIndex = i
		continue
	UserID = ss[ObserIndex]
	ObserverDate = ss[DateIndex]
	SYear = int(ObserverDate[0:4])
	if UserID in ObMatchSY:
		if ObMatchSY[UserID] > SYear:
			ObMatchSY[UserID] = SYear
	else:
		ObMatchSY[UserID] = SYear
	if UserID in ObMatchEY:
		if ObMatchEY[UserID] < SYear:
			ObMatchEY[UserID] = SYear
	else:
		ObMatchEY[UserID] = SYear
	#print UserID,ObserverDate,ObMatchSY[UserID]

outfile = open("/home/projects/ebird/BCR30/ObMatchSY.dump","w")
pickle.dump(ObMatchSY,outfile)
outfile2 = open("/home/projects/ebird/BCR30/ObMatchEY.dump","w")
pickle.dump(ObMatchEY,outfile2)


