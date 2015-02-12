import cPickle as pickle

IDmatchList = pickle.load()
IDmatchNum = pickle.load()
NummatchID = pickle.load()


ClusterN = 20
ClusterCenter = []
ClusterCenter[0] = []
Centerlabel = {}
CenterTot = []

for i in range(1,ClusterN+1):
	ClusterCenter[i] = IDmatchList[NummatchID[i]]
itMax = 20
it = 0
while it<itMax:
	it += 1
	for i in range(1,len(NumMatchID)+1):
				

	
