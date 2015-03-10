import cPickle as pickle
import math
IDmatchList = pickle.load(open("/home/projects/ebird/BCR30/IDmatchCProfile","r"))
IDmatchNum = pickle.load(open("/home/projects/ebird/BCR30/IDmatchNum","r"))
NummatchID = pickle.load(open("/home/projects/ebird/BCR30/NummatchID","r"))


ClusterN = 16
ClusterCenter = []
NewClusterCenter = []
for i in range(0,ClusterN+1):
	ClusterCenter.append([])
	for year in range(0,16):
		ClusterCenter[i].append(0)
Centerlabel = {}
CenterTot = []
IDmatchLabel = {}
for i in range(1,ClusterN+1):
	for year in range(1,15):
		ClusterCenter[i][year] = IDmatchList[NummatchID[i+100]][year]
itMax = 100
it = 0
label = {}
while it<itMax:
	it += 1
	# initialize new cluster center and 
	CenterTot = []
	NewClusterCenter = []
	CenterTot.append(0)
	NewClusterCenter.append([])
	dissubt = []
	dissubt.append(0)
	for i in range(1,ClusterN+1):
		NewClusterCenter.append([])
		for j in range(1,16):
			NewClusterCenter[i].append(0)
		CenterTot.append(0)
		dissubt.append(0)
	for i in range(1,len(NummatchID)+1):
		lab = 0
		CloseDist = 1000000
		for j in range(1,ClusterN+1):
			dis = 0
			for year in range(1,15):
				dis += (ClusterCenter[j][year] - IDmatchList[NummatchID[i]][year]) * (ClusterCenter[j][year] - IDmatchList[NummatchID[i]][year])
			dis = math.sqrt(dis)
			if dis < CloseDist:
				CloseDist = dis
				lab = j
		label[i] = lab
		CenterTot[lab] += 1
		IDmatchLabel[NummatchID[i]] = lab
		for year in range(1,15):
			NewClusterCenter[lab][year] += IDmatchList[NummatchID[i]][year]
	for i in range(1,ClusterN+1):
		if CenterTot[i] ==0: continue
		for year in range(1,15):
			NewClusterCenter[i][year] = NewClusterCenter[i][year] / CenterTot[i]
	disTot = 0
	for i in range(1,len(NummatchID)+1):
		lab = IDmatchLabel[NummatchID[i]]
		dist = 0
		for year in range(1,15):
			dist += (IDmatchList[NummatchID[i]][year] - NewClusterCenter[lab][year]) * (IDmatchList[NummatchID[i]][year] - NewClusterCenter[lab][year])
		dissubt[lab] += math.sqrt(dist)
	for i in range(1,ClusterN+1):
		if CenterTot[i]==0: continue
		dissubt[i] = dissubt[i] / CenterTot[i]
	for i in range(1,ClusterN+1):
		dissub = 0
		for year in range(1,15):
			dissub += (ClusterCenter[i][year] - NewClusterCenter[i][year]) * (ClusterCenter[i][year] - NewClusterCenter[i][year])
			ClusterCenter[i][year] = NewClusterCenter[i][year]
		disTot += math.sqrt(dissub)
	print "iteration",it,"DisTot=",disTot
	if disTot<0.0001: break

pickle.dump(IDmatchLabel,open("/home/projects/ebird/BCR30/IDmatchLabel.dump","w"))
outComp = open("/home/projects/ebird/BCR30/K-means-Compare.csv","w")
outfile = open("/home/projects/ebird/BCR30/Time-series-16-above100-Kmeans.csv","w")
for i in range(1,ClusterN+1):
	print "Cluster",i,"Tot=",CenterTot[i],"DisInCluster=",dissubt[i]
	#print ClusterCenter[i]
	for j in range(1,13):
		outfile.write(str(ClusterCenter[i][j]) + ",")
	outfile.write(str(ClusterCenter[i][13]) + "\n")
	kk = []
	for num in label:
		if label[num]==i: 
			kk.append(num)
			if (len(kk)>4): break
	#K-means Compare
	#print ClusterCenter[i],IDmatchList[NummatchID[kk]]
	for year in range(1,13):
		outComp.write(str(ClusterCenter[i][year]) + ",")
	outComp.write(str(ClusterCenter[i][year]) + "\n")
	for item in kk:
		for year in range(1,13):
			outComp.write(str(IDmatchList[NummatchID[item]][year]) + ",")
		outComp.write( str(IDmatchList[NummatchID[item]][year]) + "\n")
