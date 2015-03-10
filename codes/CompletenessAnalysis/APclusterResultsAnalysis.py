import cPickle as pickle
NummatchID = pickle.load(open("/home/projects/ebird/BCR30/NummatchID","r"))
infile = open("/home/projects/ebird/BCR30/IDmatchCProfile","r")
IDmatchList = pickle.load(infile)

infile = open("/home/projects/ebird/BCR30/idx.txt","r")

tt = 0
dic = []
count = {}
label = {}
for line in infile:
	tt += 1
	ex = int(line[0:len(line)-1])
	if tt % 100 ==0:
		print tt/100
		print IDmatchList[NummatchID[tt]],IDmatchList[NummatchID[ex]]
	if ex in count: 
		count[ex] += 1
	else: 
		count[ex] = 1
	label[tt] = ex
	if ex in dic: continue
	dic.append(ex)

tt = 0
outComp = open("/home/projects/ebird/BCR30/AP-Compare.csv","w")
outfile = open("/home/projects/ebird/BCR30/Time-series-16-above100-AP.csv","w")
for num in dic:
	tt += 1
	print tt,num,IDmatchList[NummatchID[num]],count[num]
	for i in range(1,13):
		outfile.write( str(IDmatchList[NummatchID[num]][i]) + "," )
	outfile.write( str(IDmatchList[NummatchID[num]][i]) + "\n" )
	for year in range(1,13):
		outComp.write( str(IDmatchList[NummatchID[num]][year]) + ","   )
	outComp.write( str(IDmatchList[NummatchID[num]][13]) + "\n" )
	kk = []
	ex = num
	for item in label:
		if label[item]==num:
			kk.append(item)
			if len(kk)>4: break
	for item in kk:
		for year in range(1,13):
			outComp.write( str(IDmatchList[NummatchID[item]][year])  + ",")
		outComp.write( str(IDmatchList[NummatchID[item]][13])  + "\n") 
