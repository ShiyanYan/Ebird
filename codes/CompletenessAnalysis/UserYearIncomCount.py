# build the table for user-year-completeness
import cPickle as pickle

indic = open("/home/projects/ebird/BCR30/ObMatchSY.dump","r")
ObMatchSY = pickle.load(indic)

infile = open("/home/projects/ebird/BCR30/ECR303137.txt","r")

tt = 0
ObserIndex = 0
DateIndex = 0
CompleteIndex = 0
outfile = open("/home/projects/ebird/BCR30/User-Year-Complete-Checklist.csv","w")
outfile.write("ID,Year,Complete\n")
comp = {}
incomp = {}

#EventIDdic = pickle.dump(open("/home/projects/ebird/BCR30/Temp/EventIDCounts.csv","r"))
#newdic = {}
#for item in sorted(EventIDdic):
#	newdic[item] = EventIDdic[item]
#EventIDlist = sorted(EventIDdic)
SEdic = []
def binarySearch(li,key):
	i = 0
	j = len(li) - 1
	while (i<j):
		mid = (i + j) / 2
		if li[mid]>=key:
			j = mid
		else:
			i = mid + 1
	if li[j]==key:
		return True
	else:
		return False



for line in infile:
	ss = line.split("\t")
	tt += 1
#	if tt>100000: break
	if tt % 1000000 == 0: print tt,"Complete"
	if tt==1:
		width = len(ss)
		for i in range(0,width):
			if ss[i] == "OBSERVER ID": ObserIndex = i
			if ss[i] == "OBSERVATION DATE": DateIndex = i
			if ss[i] == "ALL SPECIES REPORTED": CompleteIndex = i
			if ss[i] == "SAMPLING EVENT IDENTIFIER": SEIndex = i
		continue
	UserID = ss[ObserIndex]
	if ss[SEIndex] in SEdic : continue
	SEdic.append(ss[SEIndex])
	if not UserID in ObMatchSY: continue
	UserYear = int(ss[DateIndex][0:4]) - ObMatchSY[UserID]
	UserComplete = ss[CompleteIndex]
	if UserComplete == "1": 
		if UserYear in comp: 
			comp[UserYear] += 1
		else:
			comp[UserYear] = 1
	else:
		if UserYear in incomp:
			incomp[UserYear] += 1
		else:
			incomp[UserYear] = 1
	outfile.write(UserID + "," + str(UserYear) + "," + UserComplete + "\n") 

outfile2 = open("/home/projects/ebird/BCR30/IncompRate-Checklist.csv","w")
outfile2.write("Year,Comp,Incomp,Rate\n")
for i in range(0,30):
	outfile2.write(str(i+1) + ",")
	if i in comp:
		print i,"C",comp[i]
		outfile2.write(str(comp[i]) + ",")
	else:
		print i,"C",0
		outfile2.write(str(0) + ",")
	if i in incomp:
		print i,"IC",incomp[i]
		outfile2.write(str(incomp[i]) + ",")
	else:
		print i,"IC",0
		outfile2.write(str(0) + ",")
	if comp[i]+incomp[i]>0:
		print float(incomp[i])/float(comp[i]+incomp[i])
		outfile2.write(str(float(incomp[i])/float(comp[i] + incomp[i])) + "\n")
