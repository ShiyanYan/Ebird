#EventIDCount.py

import cPickle as pickle

inputfile = open("/home/projects/ebird/BCR30/EBD-BCR30.txt","r")


dic = {}
tt = 0
for line in inputfile:
	ss = line.split("\t")
	tt += 1
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "SAMPLING EVENT IDENTIFIER": EventIndex = i
		continue
	EventID= ss[EventIndex]
	if EventID in dic:
		dic[EventID] += 1
	else:
		dic[EventID] = 1

tempPath = "/home/projects/ebird/BCR30/Temp/"

outfile = open(tempPath + "EventIDCounts.csv","w")

outfile.write("EventID,Count\n")
for EventID in dic:
	outfile.write(EventID + "," + str(dic[EventID]) + "\n")

outfile2 = open(tempPath + "EventIDCount.dump","w")
pickle.dump(dic,outfile2)
