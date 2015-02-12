import cPickle as pickle
import math
infile = open("/home/projects/ebird/BCR30/IDmatchCProfile","r")
IDmatchList = pickle.load(infile)
IDmatchList2 = IDmatchList
IDmatchNum = pickle.load(open("/home/projects/ebird/BCR30/IDmatchNum","r"))
NummatchID = pickle.load(open("/home/projects/ebird/BCR30/NummatchID","r"))

outfile1 = open("/home/projects/ebird/BCR30/SimCos.txt","w")
tt = 0
tt2 = 0
avesim = 0
maxtt = 0
for ID in IDmatchList:
	tt += 1
	if tt % 1000==0: 
		print tt,"Complete"
		print tt2
		print maxtt
	for ID2 in IDmatchList2:
		if ID==ID2: continue
		no = 0
		deno1 = 0
		deno2 = 0
		for i in range(1,15):
			no += IDmatchList[ID][i] * IDmatchList[ID2][i]
			deno1 += IDmatchList[ID][i] * IDmatchList[ID][i]
			deno2 += IDmatchList[ID2][i] * IDmatchList[ID2][i]
		sim = float(no) / math.sqrt(float(deno1)) / math.sqrt(float(deno2))
		if sim>maxtt: maxtt = sim
		if sim>0.95: 
			outfile1.write(str(IDmatchNum[ID]) + "	" + str(IDmatchNum[ID2]) + "	" + str(sim) + "\n")
			tt2 += 1
			avesim = avesim + sim

print "Average Similarity", avesim/float(tt2)
