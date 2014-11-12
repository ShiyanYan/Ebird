#EBD-BCR30-Event-Extraction.py
import sys
import cPickle as pickle 
# EventIDs = sorted(pickle.load(open("/home/projects/ebird/BCR30/EventIDAll.dump",'r')))

# def bSearch(ks):
# 	i = 0
# 	j = len(EventIDs)-1
# 	while i<j:
# 		mid = (i + j) /2
# 		if EventIDs[mid] == ks: 
# 			return True
# 		if ks <= EventIDs[mid]:
# 			j = mid
# 		else:
# 			i = mid + 1
# 	if (EventIDs[i]==ks) or (EventIDs[j]==ks):
# 		return True
# 	else:
# 		return False

inputfile = open("/home/projects/ebird/EBD_relAug-2014/ebd_relAug-2014.txt","r")

tt = 0
ind  = 0
outputfile = open("/home/projects/ebird/BCR30/ECR303137.txt","w")
linetot = 0
InBCRTot = 0
InBCRCom = 0
OutBCRTot = 0
OutBCRCom = 0
for line in inputfile:
	tt += 1
	#if tt>100: break
	if tt % 1000000==0: print tt,"complete!",linetot
	ss = line.split("\t")
	if tt==1:
		ind = 0
		for s in ss:
			if s=="SAMPLING EVENT IDENTIFIER":
				indEvent = ind
			if s=="ALL SPECIES REPORTED":
				indComp = ind
			if s=="BCR CODE":
				indBCR = ind
			ind += 1
#		outputfile.write(line)
		continue
	if not (ss[BCR]=='37' or ss[BCR]=='30' or ss[BCR]=='31'):
		OutBCRTot += 1
		if ss[indComp]=="1": OutBCRCom += 1
	else:
		outputfile.write(line)
		InBCRTot += 1
		if ss[indComp]=="1": InBCRCom += 1

print indEvent,indComp
print "InBCR Tot=",InBCRTot,"Complete=",InBCRCom
print "OutBCR Tot=",OutBCRTot,"Complete=",OutBCRCom
#	outputfile.write(line)

