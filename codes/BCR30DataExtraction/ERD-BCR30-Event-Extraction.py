#ERD BCR30 Event Extraction
import sys
import cPickle as pickle
Event_ID_list = []
for i in range(2002,2013):
	inputfile = open("/home/projects/ebird/ERD_us48/" + str(i) + "/core-covariates.csv","r")
	tt = 0
	ind = 0

	for line in inputfile:
		ss = line.split(',')
		tt += 1
		if tt % 100000==0: print i,tt,"complete!"
		if tt == 1:
			ind = 0
			for s in ss:
				if s=='BCR':
					break
				else:
					ind += 1
			continue
		if (ss[ind]=="30"):
			Event_ID_list.append(ss[0])
print len(Event_ID_list)
outputfile = open("/home/projects/ebird/BCR30/EventIDs.dump","w")
pickle.dump(Event_ID_list,outputfile)