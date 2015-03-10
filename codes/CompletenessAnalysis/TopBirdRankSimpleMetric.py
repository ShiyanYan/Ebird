import cPickle as pickle
import math
ObMatchEY = pickle.load(open("/home/projects/ebird/BCR30/ObMatchEY.dump","r"))
ObMatchSY = pickle.load(open("/home/projects/ebird/BCR30/ObMatchSY.dump","r"))
IDmatchLabel = pickle.load(open("/home/projects/ebird/BCR30/IDmatchLabel.dump","r"))
ChecklistNum = pickle.load(open("/home/projects/ebird/BCR30/ChecklistNum.dump","r"))
IDmatchList = pickle.load(open("/home/projects/ebird/BCR30/IDmatchCProfile","r"))

outfile = open("/home/projects/ebird/BCR30/ProfilesForRankList2.4.csv","w")
LabelMLevel = {8:1,11:2,14:2,15:2,12:3,1:4,7:4,9:4,5:4,6:5,10:5,16:5,13:6,2:6,3:7,4:8}
outfile.write("ObserverID,ChecklistNumber,CurveType,StartYear,EndYear\n")
IDMscore = {}
c = 0
for ID in IDmatchLabel:
	if not ID in ChecklistNum: continue
	if not ID in ObMatchEY: continue
	score = math.log(ChecklistNum[ID]) *( LabelMLevel[IDmatchLabel[ID]] + 1) #/ math.log( 2016 - ObMatchEY[ID] )
	IDMscore[ID] = score
	if ObMatchEY[ID]==2014: c+= 1
print c
tt = 0
for ID in sorted(IDMscore,key=IDMscore.get,reverse=True):
	tt += 1
#	if tt>20: break
	if tt % 100 ==1:
		outfile.write(ID + "," + str(ChecklistNum[ID]) + "," + str(IDmatchLabel[ID]) + "," + str(ObMatchSY[ID]) + "," + str(ObMatchEY[ID]) + "\n" )
#	print ID
#	if tt % 100==1: 
#		print ID
#		print tt,IDMscore[ID],ID,ChecklistNum[ID],ObMatchEY[ID]
#		print IDmatchList[ID]

