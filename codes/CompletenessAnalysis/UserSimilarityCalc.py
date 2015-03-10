import cPickle as pickle
import math
infile = open("/home/projects/ebird/BCR30/IDmatchCProfile","r")
IDmatchList = pickle.load(infile)
IDmatchList2 = IDmatchList
IDmatchNum = pickle.load(open("/home/projects/ebird/BCR30/IDmatchNum","r"))
NummatchID = pickle.load(open("/home/projects/ebird/BCR30/NummatchID","r"))

outfile1 = open("/home/projects/ebird/BCR30/SimCos-100-0.30-E.txt","w")
tt = 0
tt2 = 0
avesim = 0
maxtt = 0
tr = 0
for ID in IDmatchList:
	tt += 1
	flag = 1
	for i in range(2,15):
		if (IDmatchList[ID][i]>0): flag = 0
#	if flag ==1: continue
	tr += 1
	if tt % 1000==0: 
		print tt,"Complete"
		print tt2
		print maxtt
	for ID2 in IDmatchList2:
		if ID==ID2: continue
		flag = 1
		for i in range(2,15):
			if (IDmatchList[ID2][i]>0): flag = 0
#		if flag==1: continue
		#no = 0
		#deno1 = 0
		#deno2 = 0
		sumdis = 0
		for i in range(1,15):
			sumdis += (IDmatchList[ID][i] - IDmatchList[ID2][i]) * (IDmatchList[ID][i] - IDmatchList[ID2][i])
			# Use Euclidean Distance  Sim = 1 / (D + 1)
			# no += IDmatchList[ID][i] * IDmatchList[ID2][i]
			# deno1 += IDmatchList[ID][i] * IDmatchList[ID][i]
			# deno2 += IDmatchList[ID2][i] * IDmatchList[ID2][i]
		sim = 1 / (1 + math.sqrt(sumdis))
		#sim = float(no) / (math.sqrt(float(deno1)) * math.sqrt(float(deno2)))
		#if sim>0.985: print IDmatchList[ID],IDmatchList[ID2]
		if sim>maxtt: maxtt = sim
		if sim>0.3: 
			outfile1.write(str(IDmatchNum[ID]) + "	" + str(IDmatchNum[ID2]) + "	" + str(sim) + "\n")
			tt2 += 1
			avesim = avesim + sim
print "TR",tr
print "Average Similarity", avesim/float(tt2)
