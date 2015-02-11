import cPickle as pickle

infile = open("/home/projects/ebird/BCR30/SubEBD303137-TruncHis.csv","r")
tt = 0
IDmatchList ={}
totOb = 0
for line in infile:
	tt += 1
	if tt==1: continue
	if tt % 1000000 ==0: print str(tt) + " Complete!"
	ss = line.split(",")
	obID = ss[1]
	Year = int(ss[3])
	if obID in IDmatchList:
		IDmatchList[obID][Year] += 1
	else:
		IDmatchList[obID] = []
		for i in range(1,16):
			IDmatchList[obID].append(0)
		IDmatchList[obID][Year] = 1
		totOb += 1

print totOb
IDmatchNum = {}
NummatchID = {}
tt = 0
for ID in IDmatchList:
	tt += 1
	maxt = 0
	for i in range(0,15):
		if IDmatchList[ID][i]>maxt: maxt = IDmatchList[ID][i]
	for i in range(0,15):
		IDmatchList[ID][i] = float(IDmatchList[ID][i])/float(maxt)
	IDmatchNum[ID] = tt
	NummatchID[tt] = ID
outfile = open("/home/projects/ebird/BCR30/IDmatchCProfile","w")

pickle.dump(IDmatchList,outfile)
outfile2 = open("/home/projects/ebird/BCR30/IDmatchNum","w")
pickle.dump(IDmatchNum,outfile2)
outfile3 = open("/home/projects/ebird/BCR30/NummatchID","w")
pickle.dump(NummatchID,outfile3)
