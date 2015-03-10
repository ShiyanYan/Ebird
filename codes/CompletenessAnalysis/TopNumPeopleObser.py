import cPickle as pickle

IDmatchList = pickle.load(open("/home/projects/ebird/BCR30/IDmatchCProfile","r"))
ChecklistNum = pickle.load(open("/home/projects/ebird/BCR30/ChecklistNum.dump","r"))
tt = 0
for ID in sorted(ChecklistNum,key=ChecklistNum.get,reverse=True):
	tt += 1
	if tt>20: break
	print ChecklistNum[ID]
	print IDmatchList[ID]
