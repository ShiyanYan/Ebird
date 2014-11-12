#EBD-BCR30-Event-Extraction.py
import sys
import cPickle as pickle 
EventIDs = sorted(pickle.load(open("/home/projects/ebird/BCR30/EventIDAll.dump",'r')))

def bSearch(ks):
	i = 0
	j = len(EventIDs)-1
	while i<j:
		mid = (i + j) /2
		if EventIDs[mid] == ks: 
			return True
		if ks <= EventIDs[mid]:
			j = mid
		else:
			i = mid + 1
	if (EventIDs[i]==ks) or (EventIDs[j]==ks):
		return True
	else:
		return False

inputfile = open("/home/projects/ebird/EBD_relAug-2014/ebd_relAug-2014.txt","r")

tt = 0
ind  = 0
outputfile = open("/home/projects/ebird/BCR30/EBD-None-ERDData.txt","w")
linetot = 0
for line in inputfile:
	tt += 1
	if tt % 1000000==0: print tt,"complete!",linetot
	ss = line.split("\t")
	if tt==1:
		ind = 0
		for s in ss:
			if s=="SAMPLING EVENT IDENTIFIER":
				break
			else:
				ind += 1
		outputfile.write(line)
		continue
	if bSearch(ss[ind]): continue
	outputfile.write(line)
	linetot += 1

